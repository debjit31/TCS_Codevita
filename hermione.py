mod = 10**9 + 7
fact = [1]
for i in range(1, 10^5+1):
    fact.append(fact[i-1] * i)

a = []
ans = []
n = int(input())
a = [int(x) for x in input().split()]
q = int(input())
while q > 0:
    l, r = input().split()
    prod = 1
    for i in  range(int(l), int(r)):
        f = fact[i]
        prod = prod * f
    prod = prod % mod
    h = prod ** (int(r)-int(1))
    print(h)
    q-=1