from collections import defaultdict
ascii = defaultdict(int)
for i in range(97, 123):
	ascii[chr(i)] = i-97+1
# print(ascii)	
for _ in range(int(input())):
	s = input()
	s_count = defaultdict(int)
	for i in s:
		s_count[i] += 1
	# print('s_count :- ', s_count)
	flag = 0
	for x in s_count:
		if s_count[x] != ascii[x]:
			flag = 1
			break
	if flag:
		print("No")
	else:
		print("Yes")
	
