num = int(input('Please Input a Num:'))
while num:
    if num > 0:
        sq = num * num
        print('Square(Num)=%d' % sq)
        num = int(input('Please Input a Num Again:'))
    else:
        num = int(input('Please Input a Num Again:'))
