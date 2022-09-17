import math

x = True
list_numbers = [] 
while x == 1:
    temp = int(input('Nhập giá trị:    '))
    list_numbers.append(temp)
    x = int(input('Tiếp tục nhập giá trị? 1: Có, 0: Không   '))

print(f'List: {list_numbers}')

#Tìm số nguyên tố
'''
Số nguyên tố là số lớn hơn 1 và chỉ chia hết cho 1 và chính nó
Số 2 là số nguyên tố chẵn duy nhất
Căn bậc 2 của số x^2 = x*x -> sét trong đoạn từ 3 đến x và bỏ qua các số chẵn
Nếu số x^2 không chia hết cho các số trong khảng sét
=> x^2 là số nguyên tố
'''
list_SNT = []
for n in list_numbers:
    if n == 2:
        list_SNT.append(n)
        continue
    if n > 1 and n % 2:
        for m in range(3, 1 + math.floor(math.sqrt(n)), 2):
            if n % m == 0:
                continue
        list_SNT.append(n)

print(f'Các số nguyên tố có trong list: {list_SNT}')

list_am = [i for i in list_numbers if i < 0]
if len(list_am):
    print(f'Các phần tử âm trong list: {list_am}')
    print(f'Trung bình cộng các phần tử âm: {sum(list_am)/len(list_am)}')

list_duong = [i for i in list_numbers if i >= 0]
if len(list_duong):
    print(f'Các phần tử dương trong list: {list_duong}')
    print(f'Trung bình cộng các phần tử dương: {sum(list_duong)/len(list_duong)}')

print(f'''Giá trị max trong list {max(list_numbers)}
Giá trị min trong list {min(list_numbers)}''')

list_numbers.sort()
print(f'List sắp tăng dần {list_numbers.sort()}')