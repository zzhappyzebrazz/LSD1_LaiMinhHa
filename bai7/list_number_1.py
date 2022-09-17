x = True
list_numbers = []
while x == 1:
    temp = int(input('Nhập giá trị:    '))
    list_numbers.append(temp)
    x = int(input('Tiếp tục nhập giá trị? 1: Có, 0: Không   '))

x = int(input('Nhập giá trị cần tìm x: '))

print(f'List :{list_numbers}')

print(f'Tổng các giá trị trong list: {sum(list_numbers)}')

if x in list_numbers:
    print(f'{x} xuất hiện {list_numbers.count(x)} lần trong list')

if x > max(list_numbers):
    print(f'{x} lớn hơn tất cả các phần tử có trong list')
else:
    print(f'{x} không lớn hơn tất cả các phần tử có trong list')
    list_lon_hon_x = [t for t in list_numbers if t > x]
    print(f'Các số lớn hơn {x} trong list: {list_lon_hon_x}')