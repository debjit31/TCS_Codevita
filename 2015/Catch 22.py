for _ in range(int(input())):
	f,b,t,fd,bd = list(map(int, input().split()))
	if f>0 and b>0 and t>0 and fd>0 and bd>0:
		td,pos = 0,0
		if f>b:
			while (pos+f) < fd:
				pos = pos + f - b
				td = td + b+f
			td = td + fd - pos
			print(td*t,'F')
		elif b>f:
			while pos+f-b >= -bd:
				pos = pos+f-b
				td = td + f + b
			if pos > -bd:
				td  = td+f+(pos+f-(-bd))
			print(td*t,'B')
		else:
			if fd > f:
				print("No Ditch")
			elif fd < f:
				print(fd,'F')
				
			
			