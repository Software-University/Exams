a = int(input())
b = int(input())
c = int(input())
d = int(input())
x = int(input())

if x == 1:
    c += 1
else:
    d += 1

if a + b >= 5 or a > 3 or b > 3:
    print ("Pesho, you are stupid!")
elif (a + b == 4) and (c > d and c >= 15 and c - d >= 2):
    print ("Match over! Team 1 is the winner!".format (a + 1, b))
elif (a + b == 4) and (c < d and d >= 15 and d - c >= 2):
    print ("Match over! Team 2 is the winner!".format (a, b + 1))
elif (a < 2) and (c > d and c >= 25 and c - d >= 2):
    print ("Game over! {0}:{1}!".format (a + 1, b))
elif (a == 2) and (c > d and c >= 25 and c - d >= 2):
    print ("Match over! Team 1 is the winner!".format (a + 1, b))
elif (b < 2) and (c < d and d >= 25 and d - c >= 2):
    print ("Game over! {0}:{1}!".format (a, b + 1))
elif (b == 2) and (c < d and d >= 25 and d - c >= 2):
    print ("Match over! Team 2 is the winner!".format (a, b + 1))
else:
    print ("Bulgarians - Heroes! {0}:{1} {2}:{3}".format (a, b, c, d))
