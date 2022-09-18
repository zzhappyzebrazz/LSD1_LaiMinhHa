import math


x = int(input('Nhập x:\n'))
if x > 1:
    # if x == 2:
    #     print(f'{x} là số nguyên tố')
    # elif x % 2 == 0:
    #     print(f'{x} không là số nguyên tố')
    # else:
    #     for i in range(3, 1 + math.floor(x ** 0.5), 2):
    #         if x % i == 0:
    #             print(f'{x} không là số nguyên tố1')
    #             break
    #         else:
    #             print(f'{x} là số nguyên tố')
    flag = 0
    if x == 2:
        print(f'{x} là số nguyên tố')
    else:
        for i in range(2, x, 1):
            if x % i == 0:
                print(f'{x} không là số nguyên tố')
                flag = 1
                break
        if not flag:
                print(f'{x} là số nguyên tố')
else:
    print('Số nhập không hợp lệ')