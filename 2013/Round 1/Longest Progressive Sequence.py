def lps(ar):
	ans = []
	tmp = [ar[0]]
	for i in range(1, n):
		if ar[i] >= tmp[-1]:
			tmp.append(ar[i])
		else:
			# print("length of tmp = ",len(tmp))
			if len(tmp) > len(ans):
				ans[:] = tmp[:]
			tmp=[]
			tmp.append(ar[i])
		# print("Tmp :- ", tmp)
		# print("Ans :- ", ans)
		
	if len(tmp) > len(ans):
		return tmp
	else:
		return ans

n = int(input())
ar = list(map(int, input().split()))
print(lps(ar))