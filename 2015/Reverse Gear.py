for _ in range(int(input())):
	f,b,t,d = list(map(int, input().split()))
	if b>f and f>0 and b>0 and t>0 and d>0:
		pos,td=0,0
		while d-(pos+b) > 0:
			pos = pos + (b-f)
			td += b + f
		td += d-pos
		print(td*t)
	else:
		print("Invalid Input")