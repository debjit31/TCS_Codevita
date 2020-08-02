x = int(input())
y = int(input())
va = int(input())
vb = int(input())
if x > 0 and y > 0 and va > 0 and vb > 0:
	dist = (x**2 + y**2)**(1/2)
	while x>=0 or y>=0:
		x = x-va
		y = y-vb
		dist = min(dist, (x**2 + y**2)**(1/2))
		# print(x)
		# print(y)
	print(dist)
else:
	print("Invalid Input")