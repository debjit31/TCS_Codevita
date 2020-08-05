
# N=20
# 1, 2, 4, 5, 10, 20
# 2, 5 , 10


def findFactors(n):
	f=[]
	for i in range(1, 1+int(n**(1/2))):
		if n % i == 0:
			if n//i == i:
				f.append(n//i)
			else:
				f.append(n//i)
				f.append(i)
	return sorted(f)

def isPrime(n):
	if n <= 1:
		return False
	elif n == 2:
		return True
	else:
		for i in range(2, 1+int(n**(1/2))):
			if n%i == 0:
				return False
		return True
		
def checkPerfectSquare(n):
	if n == 1:
		return False
	return  n**(1/2) == int(n**(1/2)) 
	
for _ in range(int(input())):
	n = int(input())
	ans = 0
	factors = findFactors(n)
	factors.pop(0)
	for i in range(len(factors)):
		if isPrime(factors[i]) == True:
			ans += 1
			# print('Prime ',factors[i])
		elif not checkPerfectSquare(factors[i]):
			sf = findFactors(factors[i])
			# print(sf)
			if any(list(map(checkPerfectSquare, sf))) == False:
				# print(factors[i])
				ans+=1
	print(ans)
				
		
