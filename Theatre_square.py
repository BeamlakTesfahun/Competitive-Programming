n,m,a = map(int,input().split())
if m%a == 0:
    v1 = m//a
else:
    v1 = m//a + 1
if n%a == 0:
    v2 = n//a
else:
    v2 = n//a + 1
print(v1*v2)
