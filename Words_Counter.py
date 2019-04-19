num = 0
str = input('Please inter some words(separated by space):')
print()
for i in str:
    if i == ' ':
        num += 1
print('num =', num+1)
