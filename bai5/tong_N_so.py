print('CT tính tổng N số nguyên')
N = int(input('N = '))
S = 0
for i in range(N):
    S += int(input(f'Nhập số nguyên thứ {i + 1}: '))
print(f'S = {S}')