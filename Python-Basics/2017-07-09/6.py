n = int(input ())

while n > 0:
    prevFib = 1
    currFib = 1
    nextFib = 2
    while nextFib <= n:
        nextFib = prevFib + currFib
        prevFib = currFib
        currFib = nextFib
    n -= prevFib
    print (prevFib)
