#from numba import njit

#@njit
def strippowers(r,x,y,alpha,beta):
    if x%2==0 and y%2==0:
      x,y= x//2,y//2
    else:
      x,y = (x+beta)//2,(y-alpha)//2
    return r//2, x, y

#@njit
def EBEA(a,b):
  ap = abs(a)
  bp = abs(b)
  d=1
  x1,y1,x2,y2 = 1,0,0,1
  while (ap%2==0 and bp%2==0):
    ap=ap//2
    bp=bp//2
    d*=2
  alpha = ap
  beta = bp
  
  while ap%2==0:
    ap, x1, y1 = strippowers(ap, x1, y1, alpha, beta)
  while bp%2==0:
    bp, x2, y2 = strippowers(bp, x2, y2, alpha, beta)
  if ap < bp:
    ap,x1,y1, bp,x2,y2 = bp,x2,y2, ap,x1,y1
  while bp >0:
    ap=ap-bp
    x1,y1=x1-x2,y1-y2
    while ap%2==0 and ap>0:
      ap,x1,y1 = strippowers(ap,x1,y1,alpha,beta)
    if ap<bp:
      ap,x1,y1, bp,x2,y2 = bp,x2,y2, ap,x1,y1
  if a<0:
    x1,x2 = -x1,-x2
  if b<0:
    y1,y2=-y1,-y2
  return d*ap, x1, y1
