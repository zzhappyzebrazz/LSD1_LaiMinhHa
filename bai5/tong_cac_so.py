S = 0
print('CT tính tổng các số nguyên')
x = int(input('Nhập một số nguyên (kết thúc là số 0): '))
while x:
    S += x
    x = int(input('Nhập một số nguyên (kết thúc là số 0): '))
print(f'S = {S}')