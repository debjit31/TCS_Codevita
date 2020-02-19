mod = 10**9 + 7
fact = [1]
for i in range(1, 10**5+1):
    fact.append((fact[i-1] * i)%mod)

a = []
n = int(input())
a = [int(x) for x in input().split()]
q = int(input())
ans = [fact[a[0]]]
for i in range(1,len(a)):
    ans.append(fact[a[i]])
print(ans)
while q > 0:
    l, r = input().split()
    prod = 1
    for i in  range(int(l), int(r)+1):
        prod = (prod * ans[i])%mod
    prod = prod % mod
    h = prod ** (int(r)-int(1))
    print(h)
    q-=1