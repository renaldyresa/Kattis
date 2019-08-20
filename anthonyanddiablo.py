import math
a,n = map(float,input().split())
r = n/(math.pi*2)
ar = math.pi* r**2
print("Diablo is happy!" if  a <= ar  else "Need more materials!")
