import random

ran = random.randint(0, 100)
num = int(input('Please Input a Num Range in 0-100\n'))
if ran > num:
    print('The Num You Have Input Less Than The Answer')
elif ran < num:
    print('The Num You Have Input Large Than The Answer')
else:
    print('Congratulations! You Have Won The Game')
