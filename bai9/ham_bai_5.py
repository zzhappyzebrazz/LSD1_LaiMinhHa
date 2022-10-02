import math

def countdown():
    count = int(input('Input number:\n'))
    for i in range(count, 0, -1):
        print(i)
    print('Start!')

def CT_tinh_bieu_thuc():
    n = int(input('Nhập n:\n'))
    '''
    A = tổng các số lẻ nhỏ hơn hay bằng n
    B = tổng các số chẵn nhỏ hơn hay bằng n
    C = tích các số từ 1 đến n
    D = tích các số chia hết cho 3 nhỏ hơn hay bằng n
    E = tổng các số nguyên tố nhỏ hơn hay bằng n
    '''
    A = [i for i in range(n + 1) if i%2]
    B = [i for i in range(1, n + 1) if not i%2]
    D = [i for i in range(1,n + 1) if not i%3]
    E = []

    for i in range(2, n ,1):
        flag = 0
        if i == 2:
            E.append(i)
        else:
            for j in range(2, i, 1):
                if i % j == 0:
                    # print(f'{x} không là số nguyên tố')
                    flag = 1
                    break
            if not flag:
                    E.append(i)

    print(f'A = {A} = {sum(A)}')
    print(f'B = {B} = {sum(B)}')
    C = 1
    for i in range(1, n + 1, 1):
        C *= i
    print(f'C = {[i for i in range(1, n + 1, 1)]} = {C}')
    print(f'D = {D} = {sum(D)}')
    print(f'E = {E} = {sum(E)}')

def kt_so_nguyen_to():
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

def tinh_A():
    n = int(input('Nhập n:\n'))
    x = int(input('Nhập x:\n'))
    A = (x * x + x + 1) ** n + (x * x - x + 1) ** n
    print(f'A = (x^2 + x + 1)^n + (x^2 - x + 1)^n = {A}')

def tinh_S():
    n = int(input('Nhập n:\n'))
    x = int(input('Nhập x:\n'))
    S = (x * x + 1) ** n
    print(f'S = (x * x + 1)^n = {S}')

def tong_cac_so():
    S = 0
    print('CT tính tổng các số nguyên')
    x = int(input('Nhập một số nguyên (kết thúc là số 0): '))
    while x:
        S += x
        x = int(input('Nhập một số nguyên (kết thúc là số 0): '))
    print(f'S = {S}')

def tong_N_so():
    print('CT tính tổng N số nguyên')
    N = int(input('N = '))
    S = 0
    for i in range(N):
        S += int(input(f'Nhập số nguyên thứ {i + 1}: '))
    print(f'S = {S}')
    
    