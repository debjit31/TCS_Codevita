def findQualities(mat, i,j):
	if i<0 or i>=n or j<0 or j>=m or mat[i][j] == 0:
		return 0
	else:
		return mat[i][j]

n,m = list(map(int, input().split()))
mat = []
for i in range(n):
	mat.append(list(map(int, input().split())))
rp = [(1,0), (-1,0), (0,1), (0,-1), (-1,-1), (1,-1), (-1,1), (1,1)]
b = [[0 for j in range(m)] for i in range(n)]
mat[0][0] = 0
maxq = -99999
for i in range(n):
	for j in range(m):
		if mat[i][j] == 1:
			nc = 0
			for p in rp:
				nc += findQualities(mat, i+p[0], j+p[1])
			# print(nc, '({},{})'.format(i+1, j+1))
			maxq = max(maxq, nc)
			b[i][j] = nc
brideFound = False
for i in range(len(b)):
	for j in range(len(b[0])):
		if b[i][j] == maxq:
			print('{}:{}:{}'.format(i+1,j+1,maxq))
			brideFound = True
			break
	if brideFound == True:
		break
if brideFound == False:
	print('No suitable girl found')
		
	
			
			