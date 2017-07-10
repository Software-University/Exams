import math

bunkerX = float(input())
bunkerY = float(input())

n = int(input())

bunkerZdravo = int(input())

ngMin = float(input())
ngMax = float(input())

ccMin = float(input())
ccMax = float(input())

ngPuc = 0
ccPuc = 0

for i in range(2*n):
	zalpX = float(input())
	zalpY = float(input())
	if i % 2 == 0:
		if ngMin <= math.sqrt((bunkerX - zalpX) * (bunkerX - zalpX) + (bunkerY - zalpY) * (bunkerY - zalpY)) <= ngMax:
			ngPuc += 1
			bunkerZdravo -= 1
			if bunkerZdravo == 0:
				print('NO\nNG')
				break
	else:
		if ccMin <= math.sqrt((bunkerX - zalpX) * (bunkerX - zalpX) + (bunkerY - zalpY) * (bunkerY - zalpY)) <= ccMax:
			bunkerZdravo -= 1
			ccPuc += 1
			if bunkerZdravo == 0:
				print('NO\nCC')
				break

if bunkerZdravo > 0:
	print("YES")
	print(ccPuc)
	print(ngPuc)
