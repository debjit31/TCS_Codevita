try:
	b, n = list(map(int, input().split()))
	ar = list(map(int, input().split()))
	dead = False
	for i in ar:
		if b>=i:
			b -= (i%2 + i//2)
		else:
			dead = True
			break
	if dead:
		print("NO")
	else:
		print("YES")
except Exception:
	print("Invalid Input")
