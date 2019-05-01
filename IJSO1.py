p = int(input())
f = [int(x) for x in input().split() ]
lifeOdd = p
lifeEven = p
checkOdd = 0
checkEven = 0
for x in f:
    if x % 2 == 0:
        checkOdd += 1
        checkEven = 0
    else:
        checkEven += 1
        checkOdd = 0

    if checkEven >= 3:
        lifeOdd -= 3
    elif checkEven == 1 or checkEven == 2:
        lifeOdd -= 1
    
    if checkOdd >= 3:
        lifeEven -= 3
    elif checkOdd == 1 or checkOdd == 2:
        lifeEven -= 1
    
    if lifeEven <= 0:
        res = x
        win = 0
        break
    if lifeOdd <= 0:
        res = x
        win = 1
        break
print(win)
print(res)