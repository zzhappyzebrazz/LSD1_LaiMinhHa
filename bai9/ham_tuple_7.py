def tuple_numbers():
    Tuple_a = (3, 1, 2, 4)
    Tuple_b = (5, 7, 6, 8)
    Tuple_c = Tuple_a + Tuple_b
    Tuple_d = list(Tuple_c)
    Tuple_d.sort()
    Tuple_d = tuple(Tuple_d)

    print(f'Tuple a: {Tuple_a}')
    print(f'Tuple b: {Tuple_b}')
    print(f'Tuple c: {Tuple_c}')
    print(f'Tuple d: {Tuple_d}')
    print(f'Tuple[3] = {Tuple_d[3]}')
    print(f'3 phần tử cuối cùng của tuple d {Tuple_d[-3:]}')
    
    
def tuple_strings():
    Tuple = ('red', 'green', 'yellow', 'blue', 'black', 'white', 'pink', 'orange', 'red', 'blue')
    index_duong = int(input('Nhập số từ 0 đến 9: '))
    index_am = int(input('Nhập số từ -1 đến -9: '))
    s_find = input('Nhập chuỗi cần tìm:\n')
    print(f'Tuple[{index_duong}] = {Tuple[index_duong]}')
    print(f'Tuple[{index_am}] = {Tuple[index_am]}')
    print(f'{s_find} xuất hiện trong tuple {Tuple.count(s_find)} lần')