import math

arrivals = ['Adela', 'Fleda', 'Owen', 'May', 'Mona', 'Gilbert', 'Fort']
meals_1 = ['Redneck Ribs', 'Prawn Star', 'San Quentin Squid', 'First Full of Pizza', 'Honky Tonk Chicken']
meals_2 = ['Redneck Ribs', 'Prawn Star', 'Running Bear Salmon', 'Running Bear Salmon', 'Honky Tonk Chicken']
nums = [2, 6, 7, 9]

def party_late (arrivals, name):
    so_khach = len(arrivals)
    # print(arrivals[math.floor(so_khach/2) : so_khach - 1])
    if name in arrivals[math.floor(so_khach/2) : so_khach - 1]:
        return True
    return False
    
def list_of_animal():
    list_of_animals = [animals for animals in input('Nhập và tên các con vật: ').split()]
    print(f'List of animals: {list_of_animals}')
    print(f'Number of animals: {len(list_of_animals)}')
    animals = input('I want to find:\n')
    if animals in list_of_animals:
        print(f'There is {animals} in list of anials')
    else:
        print(f'There is no {animals} in list of anials')
        
def menu_is_boring(meals):
    for i in meals:
        if meals.count(i) >= 2:
            return True
    return False

def has_lucky_number (nums):
    print(has_lucky_number(nums))
    for i in nums:
        if not (i % 7):
            return True
    return False
    

def list_numbers_1():
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

def list_numbers_2():
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

def list_numbers_3():
    list_numbers = [74, 74, 72, 72, 73, 69, 69, 71, 76, 71]
    print('list_number: ',list_numbers)
    so_phan_tu = len(list_numbers)
    list_met = [x * 0.0254 for x in list_numbers if x]
    print('list_met: ', list_met)

    print(f'3 chiều cao đầu tiên: {list_met[0]:.2f}m, {list_met[1]:.2f}m, {list_met[2]:.2f}m')
    print(f'3 chiều cao cuối cùng: {list_met[so_phan_tu -3]:.2f}m, {list_met[so_phan_tu -2]:.2f}m, {list_met[so_phan_tu -1]:.2f}m')
    print(f'Chiều cao trung bình: {sum(list_met)/so_phan_tu:.2f}m')
    list_met.sort();
    print(f'Chiều cao theo giá trị tăng dần: ', end="")
    for i in range(so_phan_tu):
        if i == so_phan_tu -1:
            print('%.2fm' %list_met[i])
        else:
            print('%.2fm' %list_met[i], end=', ')
    list_met.reverse()
    print(f'Chiều cao theo giá trị giảm dần: ', end="")
    for i in range(so_phan_tu):
        if i == so_phan_tu -1:
            print('%.2fm' %list_met[i])
        else:
            print('%.2fm' %list_met[i], end=', ')

def elementwise_greater_than (L, thresh):
    result = ['True' if i > thresh else 'False' for i in L]
    return result
            