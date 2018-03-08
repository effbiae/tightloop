from subprocess import *
from re import *
from time import *
import os
from terminaltables import *
from functools import *
from getopt import getopt
from sys import *
from statistics import median

from sqlite3 import dbapi2 as sql
class med:
    def __init__(self): self.x = []
    def step(self, a): self.x.append(a)
    def finalize(self): return median(self.x)
class gmean:
    def __init__(self): self.x = []
    def step(self, a): self.x.append(a)
    def product(self):  return reduce(lambda x,y:x*y,self.x)
    def finalize(self): return pow(self.product(),1/len(self.x))
conn = sql.connect(':memory:')
import math
conn.create_function("log10",1,math.log10)
conn.create_function("sqrt",1,math.sqrt)
conn.create_aggregate("median",1,med)
conn.create_aggregate("gmean",1,gmean)
conn.create_function("pow",2,math.pow)
conn.create_function("pow10",1,lambda x:math.pow(10,x))
c = conn.cursor()

g=0
optlist, args = getopt(argv[1:], 'r:o:')
oo=dict(r=1,o=7)
oo.update(dict([(x[0][1],float(x[1])) for x in optlist]))
print(oo)

#tim - find the time and result given exe, test, n and seed
def tim(exe,test,n,seed):
  t=-1;rc=-1;r=0
  env=dict(os.environ,TIMEFORMAT='%R %U %S')
  cmd=' '.join(['time',exe,str(test),str(n),str(seed)])
  p=Popen([cmd], stdout=PIPE, stderr=PIPE, shell=True, executable="/bin/bash",env=env)
  try:
    (o,e)=p.communicate(timeout=oo['o'])
  except TimeoutExpired:
    p.kill()
    (o,e)=p.communicate()
    return 0
  rc=p.returncode
  if(g):print(cmd,'returned',str(rc),"out",o)
  if rc==0:
    r=int(fullmatch(b'[0-9]+\n',o).group(0))
  b=b'([0-9.]+)[^ ]* '
  try:
    t,u,s=[float(x) for x in ((match(b+b+b[:-1],e).group(1,2,3)))]
  except Exception:
    print(e)
    raise Exception("match")
  return [exe,test,n if n<32 and not rc else -1,seed,r,t]

#reach - increase n until time exceeds 1 second
def reach(exe,test):
  n=1;t=-1;rc=-1;seed=-1;r=0
  while n<32:
    seed=int(1e9*clock_gettime(CLOCK_MONOTONIC_RAW)%pow(2,31))
    r=tim(exe,test,n,seed)
    if r[-1]>oo['r']:break
    n+=1
  return r

def gmean(a):
  return reduce(lambda x,y:x*y,a)**(1.0/len(a))
def tims(exe,test,n,seeds):
  x=[tim(exe,test,n,seed)for seed in seeds]
  return x[0][:-1]+[round(gmean([a[-1]for a in x]),3)]
def tab(c,sql="select * from t"):
  c.execute(sql)
  cols=[x[0] for x in c.description]
  t=AsciiTable([cols]+c.fetchall())
  for x in range(len(cols)):t.justify_columns[x]='right'
  print(t.table)

r=[reach('./ref',x) for x in range(3)]
T=([tims(*r[:3]+[[r[3]]*3]) for r in r])
c.execute('create table t(exe,test,n,seed,result,time)')
c.executemany("insert into t values(?,?,?,?,?,?)",T)
tab(c)

t=['jfa','cpp']
U=([[[x]+tims(*['./contrib/'+x+'/'+x]+r[1:3]+[[r[3]]*3])[1:]for r in r]for x in t*3])
[c.executemany('insert into t values(?,?,?,?,?,?)',x) for x in U]
tab(c,'select * from t order by test,n,time asc')

c.execute('select exe,pow10(sum(time)) from (select exe,test,log10(time)as time from t)group by exe order by time')
tab(c,'select exe,gmean(time) from (select exe,test,median(time) as time from t group by exe,test) group by exe order by time')
