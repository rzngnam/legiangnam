def cap_so_cong(x):
    y = 2
    arr = []
    error = 'Nhập lỗi'
    if x < 0:
        return error
    elif x == 0:
        return []
    else:
        for i in range(x):
            if i % 2 == 0:
                arr.append(y)
                y = y - 0.5
            else:
                arr.append(-1)

        return arr
