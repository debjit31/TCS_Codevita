for _ in range(int(input())):
	N,T = list(map(int, input().split()))
	E = list(map(int, input().split()))
	p, D = list(map(int, input().split()))
	t=0
	timeout = False
	dead = False
	for i in range(len(E)):
		if t < T:
			if p >= E[i]:
				p = p + (p-E[i])
				t+=1
			else:
				dead = True
				break
		elif t>=T and i < len(E)-1:
			timeout = True
			break
	if dead==True or timeout == True or p<D:
		print("No")
	else:
		print("Yes")
		