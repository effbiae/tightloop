from subprocess import *
from re import *
from time import *
import os

#reach - increase n until time exceeds 1 second
def reach(exe,test):
  n=1;t=-1;rc=-1;seed=-1;r=0
  while n<32:
    seed=int(1e9*clock_gettime(CLOCK_MONOTONIC_RAW)%pow(2,31))
    env=dict(os.environ,TIMEFORMAT='%R %U %S')
    p=Popen([' '.join(['time',exe,str(seed),str(test),str(n)])], stdout=PIPE, stderr=PIPE, shell=True, executable="/bin/bash",env=env)
    try:
      (o,e)=p.communicate(timeout=3)
    except TimeoutExpired:
      p.kill()
      (o,e)=p.communicate()
      return 0
    rc=p.returncode
    if rc!=0:break
    r=int(fullmatch(b'[0-9]+\n',o).group(0))
    b=b'([0-9.:]+)[^ ]* '
    t,u,s=[float(x) for x in ((match(b+b+b[:-1],e).group(1,2,3)))]
    if t>1:break
    n+=1
  return (n if n<32 and not rc else -1,t,seed,r)


print(reach('./ref',0))
