import bisect as bi
def findPrimes(n):
	primes = [True for i in range(n+1)]
	p=2
	while p*p <= n:
		for i in range(p*p, n+1, p):
			if primes[i] == True:
				primes[i] = False
		p+=1
	ans = []
	for i in range(2, n+1):
		if primes[i]:
			ans.append(i)
	return ans

def gameofNumber(n):
	while len(str(n)) != 1:
		y = str(n)
		s=0
		for i in y:
			s += int(i)**2
		n=s
	return n
	
for _ in range(int(input())):
	try:
		x = int(input())
		y = int(input())
		n = int(input())
		if x<=y and x>0 and y>0:
			pn = findPrimes(y)
			li = bi.bisect(pn, x)
			ri = bi.bisect(pn, y)
			pa = pn[li:ri]
			aa = []
			for i in range(len(pa)):
				xn = gameofNumber(pa[i])
				if xn == 1 or xn == 4:
					aa.append(pa[i])
			print(aa)
			if n > len(aa):
				print("No number is present at this index")
			else:
				print(aa[n-1])
		
	except Exception:
		print("Invalid Input")
	