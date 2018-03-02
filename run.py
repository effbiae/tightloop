from subprocess import *
from re import *
from time import *

#reach - increase n until time exceeds 1 second
def reach(exe,test):
  n=1;e=-1;rc=-1;seed=-1;r=0
  while n<32:
    seed=int(1e9*clock_gettime(CLOCK_MONOTONIC_RAW)%pow(2,31))
TIMEFORMAT=%R\ %U\ %S
    p=run(['time',exe,str(seed),str(test),str(n)], stdout=PIPE, stderr=PIPE, shell=True, )
    rc=p.returncode
    if rc:break
    r=int(fullmatch(b'[0-9]+\n',p.stdout).group(0))
    #print("n=",n,p.stdout)
    b=b'([0-9.:]+)[^ ]* '
    u,s,e=[float(x) for x in ((match(b+b+b"0:"+b,p.stderr).group(1,2,3)))]
    #print(u,s,e)
    if e>1:break
    n+=1
  return (n if n<32 and not rc else -1,e,seed,r)


print(reach('./ref',0))
