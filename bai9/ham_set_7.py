def set_numbers():
    set_1 = set()
    set_2 = set()

    x = 1
    while x == 1:
        temp = int(input('Nhập giá trị cho element trong set 1: '))
        set_1.add(temp)
        x = int(input('Bạn có tiếp tục nhập set 1? 1: có, khác 1: không '))
                    
    y = 1
    while y == 1:
        temp = int(input('Nhập giá trị cho element trong set 2: '))
        set_2.add(temp)
        y = int(input('Bạn có tiếp tục nhập set 2? 1: có, khác 1: không '))
                    
    print(f'Set 1: {set_1}')
    print(f'Set 2: {set_2}')
    print(f'Chiều dài Set 1: {len(set_1)}')
    print(f'Chiều dài Set 2: {len(set_2)}')
    print(f'Tổng Set 1: {sum(set_1)}')
    print(f'Tổng Set 2: {sum(set_2)}')
    print(f'Max Set 1, Min Set 1: {max(set_1)}, {min(set_1)}')
    print(f'Max Set 2, Min Set 2: {max(set_2)}, {min(set_2)}')
    print(f'Pop Set 1: {set_1.pop()}')
    print(f'Set 1 sau khi pop: {set_1}')
    Set_union = set_1 | set_2
    print(f'Set 1 union Set 2: {Set_union}')
    Set_intersection = set_1 & set_2
    print(f'Set 1 intersection Set 2: {Set_intersection}')
    Set_difference = set_1 - set_2
    print(f'Set 1 difference Set 2: {Set_difference}')
    Set_symmetric_difference = set_1 ^ set_2
    print(f'Set 1, Set 2 symmetric difference: {Set_symmetric_difference}')
    print(f'Set 1 tăng dần: {sorted(set_1)}')
    print(f'Set 2 giảm dần: {sorted(set_2, reverse = True)}')