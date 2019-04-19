while True:
    str = input("please input a string:")
    length = len(str)
    # 定义左右‘指针’
    left = 0
    right = length-1
    while left <= right:
        if str[left] == str[right]:
            left += 1
            right -= 1
        else:
            break
    if left > right:
        print("yes")
    else:
        print("no")
