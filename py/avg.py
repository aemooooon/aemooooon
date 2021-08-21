def get_average_valid_marks():
    flag = True
    marks = []
    result = 0
    while flag:
        user_input = input("Enter a mark between 0 and 100, or STOP to exit: ")
        # 如果用户输入 stop，我们把输入的转换成大写，然后跟 ‘STOP’比较，如果是 stop 就设置 flag 为 False，这样就会退出 while 循环
        if user_input.upper() == 'STOP':
            flag = False
        else:
            # 如果用户输入的是数字，我们在这里把输入的数字转换成 float 类型
            f_user_input = float(user_input)

            # 检查如果用户输入的数 不在 0-100 之间，就提示无效输入
            # 否则，把这个有效的数添加到数组里
            if f_user_input < 0 or f_user_input > 100:
                pass
            else:
                marks.append(f_user_input)

    for mark in marks:
        result += mark

    avg = result/len(marks)

    return avg


print(get_average_valid_marks())
