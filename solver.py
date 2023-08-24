from sys import stdin

input = stdin.readline

def valid_ind(i):
	if 0 <= i <= 2:
		return 0
	elif 3 <= i <= 5:
		return 1
	elif 6 <= 7 <= 8:
		return 2

def rec(i, j):
	if i == 8 and j >= 9:
		for i in sudo:
			print(*i)
		return
	if i == 9:
		rec(0, j+1)
	elif (i, j) not in fixed and i < 9 and j < 9:
		for pos in range(1, 10):
			x, y = valid_ind(i), valid_ind(j)
			if not row[i][pos-1] and not col[j][pos-1] and pos not in checker[x][y]:
				checker[x][y].add(pos)
				row[i][pos-1], col[j][pos-1] = 1, 1
				sudo[i][j] = pos
				rec(i+1, j)
				row[i][pos-1], col[j][pos-1] = 0, 0
				sudo[i][j] = 0
				checker[x][y].remove(pos)
	else:
		rec(i+1, j)


def main():
	print('Enter the board')
	global sudo, row, col, fixed, checker
	sudo = [list(map(int, input().split())) for _ in range(9)]
	checker = [[set() for _ in range(3)] for _ in range(3)]
	row = [[0 for _ in range(9)] for _ in range(9)]	
	col = [[0 for _ in range(9)] for _ in range(9)]
	fixed = set()
	for i in range(9):
		for j in range(9):
			if sudo[i][j]:
				checker[valid_ind(i)][valid_ind(j)].add(sudo[i][j])
				fixed.add((i, j))
				row[i][sudo[i][j]-1] = 1
				col[j][sudo[i][j]-1] = 1
	rec(0, 0)
	print()

if __name__  == "__main__":
	main()
