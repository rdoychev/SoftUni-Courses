x = 121

if x < 0:
    print(False)
else:
    num = x
    rev = 0
    while num != 0:
        print(x, num, rev)
        rev = rev * 10 + num % 10
        num = num // 10

    if x == rev:
        print(True)
    else:
        print(False)
