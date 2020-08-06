from collections import Counter
def checkSubstring(y):
	## check for anagram substring
	y_count = Counter(y)
	s_count = Counter()
	found = False
	for i in range(len(x)):
		s_count[x[i]] += 1
		if i>=len(y):
			if s_count[s[i - len(y)]] == 1:
				del s_count[s[i-len(y)]]
			else:
				s_count[s[i - len(y)]] -= 1
		if s_count == y_count:
			print("YES")
			found =True
			break
	if found == False:
		print("NO")


s = input()
x=s
firstchar = ""
for i in range(int(input())):
	d,r= list(map(str, input().split()))
	if d == 'L':
		s = s[int(r):] + s[0:int(r)]
		# print(s)
		firstchar += s[0]
	elif d == 'R':
		s = s[(len(s)-int(r)):] + s[0:(len(s)-int(r))]
		# print(s)
		firstchar += s[0]
checkSubstring(firstchar)
	