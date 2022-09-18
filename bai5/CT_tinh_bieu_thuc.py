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