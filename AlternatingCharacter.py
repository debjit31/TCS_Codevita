t = int(input())
while t > 0:
    s = input()
    d=0
    for i in range(len(s)):
        if i!=0 and s[i] == s[i-1]:
            d+=1
    print(d)
    t-=1