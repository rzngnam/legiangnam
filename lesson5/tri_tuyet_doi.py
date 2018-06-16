x = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def tri_tuyet_doi():
    tong = 0
    for i in range(len(x)):
        tong += abs(x[i])
    return tong

