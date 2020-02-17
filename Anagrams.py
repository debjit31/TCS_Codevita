d = 0
a = input()
b = input()
for i in 'abcdefghijklmnopqrstuvwxyz':
    d += abs(a.count(i) - b.count(i))
print(d)