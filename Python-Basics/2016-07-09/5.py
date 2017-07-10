n = int(input())
m = int(input())
q = int(input())

print('|' + (2*n + 1) * '-' + '|')
for i in range(m):
	print('|.', end='')
	curr = 0
	while q > 0 and curr < n:
		curr += 1
		q -= 1
		print('X.', end='')
	while curr < n:
		curr += 1
		print('O.', end='')
	print('|')
print('|' + (2*n + 1) * '-' + '|')
print('v' + (2*n + 1) * ' ' + 'v')
