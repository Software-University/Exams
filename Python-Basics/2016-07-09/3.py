h1 = int(input())
m1 = int(input())
h2 = int(input())
m2 = int(input())
h3 = int(input())
m3 = int(input())
p1 = int(input())
p2 = int(input())
p3 = int(input())

dur = 1 * 60 + 29

t1 = h1 * 60 + m1
t2 = h2 * 60 + m2
t3 = h3 * 60 + m3

ans = max(p1, p2, p3)

if t1 + dur <= t2:
    ans = max(ans, p1 + p2)
if t2 + dur <= t3:
    ans = max(ans, p2 + p3)
if t1 + dur <= t3:
    ans = max(ans, p1 + p3)
if t2 + dur <= t1:
    ans = max(ans, p1 + p2)
if t3 + dur <= t2:
    ans = max(ans, p2 + p3)
if t3 + dur <= t1:
    ans = max(ans, p1 + p3)

print (ans)

