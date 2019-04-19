total = 21
while True:
    print('Left:', total)
    n1 = int(input('How Many Sticks You Wanna Take(1-4):'))
    if total == 1:
        print('Sorry You Have Failed Python !')
        break
    if n1 >= 5 or n1 <= 0:
        print('Please Input a Num Range in 1-4')
        continue
    n2 = 5-n1
    print('Python has taken %d' % n2)
    total -= 5
