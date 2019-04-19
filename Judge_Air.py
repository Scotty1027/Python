pm = int(input('Please Input The PM Today:'))
if 0 <= pm < 35:
    print('空气优质，快去户外运动!')
elif 35 <= pm < 75:
    print('空气良好，适度户外活动！')
else:
    print('空气污染，请小心！')
