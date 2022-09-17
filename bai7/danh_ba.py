danh_ba = {
            'Jack' : '0933753654',
            'Misu' : '0913753951',
            'Johnny' : '0989741258',
            'Katherin' : '0903852147'
          }

while(True):
    lua_chon = int(input('Bạn muốn làm gì? 1: Xem danh bạ; 2: Tìm kiếm, 3:Thêm mới\n'))
    if lua_chon == 1:
        print('Danh bạ điện thoại:\nTên      Số điện thoại')
        for i in danh_ba:
            print(f'{i}  --  {danh_ba[i]}')
        tiep_tuc = int(input('Tiếp tục lựa chọn? 1: Có; 0: Không\n'))
        if tiep_tuc == 1:
            continue
        break
    elif lua_chon == 2:
        ten_can_tim = input('Nhập tên cần tìm:\n')
        if ten_can_tim in danh_ba:
            print(f'{ten_can_tim} có số điện thoại là {danh_ba[ten_can_tim]}')
        else:
            print(f'Không tìm thấy {ten_can_tim} danh bạ')
        tiep_tuc = int(input('Tiếp tục lựa chọn? 1: Có; 0: Không\n'))
        if tiep_tuc == 1:
            continue
        break
    elif lua_chon == 3:
        ten = input('Nhập tên:\n')
        so_dien_thoai = input('Nhập số điện thoại:\n')
        danh_ba[ten] = so_dien_thoai
        # danh_ba = sorted(danh_ba.keys())
        print('Danh bạ điện thoại')
        for i in danh_ba:
            print(f'{i}  --  {danh_ba[i]}')
        tiep_tuc = int(input('Tiếp tục lựa chọn? 1: Có; 0: Không\n'))
        if tiep_tuc == 1:
            continue
        break        
    else:
        print('Mời chọn đúng giá trị')