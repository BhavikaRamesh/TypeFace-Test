import sys
sys.setrecursionlimit(10 ** 7)

def countIslands(l, r, c, x8, y8):
	count = 0
	for i in range(r):
		for j in range(c):
			if l[i][j] == 1:
				dfs(l, i, j, r, c, x8, y8)
				count += 1
	return count
	
def dfs(l, i, j, r, c, x8, y8):
	if (i < 0) or (j < 0) or (i >= r) or (j >= c):
		return 
	if l[i][j] == 0:
		return 
	l[i][j] = 0
	for d in range(8):
		dfs(l, i + x8[d], j + y8[d], r, c, x8, y8)
	
x8 = [-1, -1, 0, 1, 1, 1, 0, -1]
y8 = [0, -1, -1, -1, 0, 1, 1, 1]

l = [[0, 0, 1], [0, 0, 0], [1, 0, 0]]
r = len(l)
c = len(l[0])
print(countIslands(l, r, c, x8, y8))