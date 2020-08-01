def rotateMatrixby90(mat):
	for i in range(n//2):
		for j in range(i, n-i-1):
			tmp = mat[i][j]
			mat[i][j] = mat[n-1-j][i]
			mat[n-1-j][i] = mat[n-1-i][n-1-j]
			mat[n-1-i][n-1-j] = mat[j][n-1-i]
			mat[j][n-1-i] = tmp

mat = []
rot = 0
n = int(input())
for i in range(n):
	mat.append(list(map(int, input().split())))
tmp = mat
while True:
	inp = list(map(str, input().split()))
	if inp[0] == '-1':
		break
	else:
		if inp[0] == 'A':
			s = int(inp[1])
			for i in range(s//90):
				rotateMatrixby90(mat)
				rot+=1
		elif inp[0] == 'Q':
			k,l = int(inp[1]), int(inp[2])
			print(mat[k-1][l-1])
		elif inp[0] == 'U':
			x,y,z = int(inp[1]), int(inp[2]), int(inp[3])
			tmp[x-1][y-1] = z
			mat = tmp
			for r in range(rot):
				rotateMatrixby90(mat)