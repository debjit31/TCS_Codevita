from collections import defaultdict
n = int(input())
comm = defaultdict(set)
comc = 1
while True:
	query = list(map(str, input().split()))
	if query[0] == '-1':
		break
	else:
		if query[0] == 'C':
			i,j = int(query[1]), int(query[2])
			if len(comm) == 0:
				comm[comc] = set([i,j])
				comc+=1
			else:
				added = False
				newc = [i,j]
				for i in comm:
					if len(set(newc) & comm[i]) != 0:
						comm[i].add(newc[0])
						comm[i].add(newc[1])
						added = True
						break
				if added == False:
						comm[comc] = set(newc)
						comc+=1
		elif query[0] == 'Q':
			emc = 0
			for i in comm:
				if len(comm[i]) % 2 == 0:
					emc+=1
			print(emc)
# print(comm)