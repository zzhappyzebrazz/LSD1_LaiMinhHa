tu_dien = {
    'cat' : 'con mèo',
    'dog' : 'con chó',
    'ant' : 'con kiến',
    'bear' : 'con gấu'
}

while(True):
    lua_chon = int(input('Bạn muốn làm gì? 1: Xem từ điển; 2: Tra từ, 3:Thêm từ, 4: Xóa từ\n'))
    if lua_chon == 1:
        print('Dictionary:\nTừ Anh      Nghĩa Việt')
        for i in tu_dien:
            print(f'{i}         {tu_dien[i]}')
        tiep_tuc = int(input('Tiếp tục lựa chọn? 1: Có; 0: Không\n'))
        if tiep_tuc == 1:
            continue
        break
    elif lua_chon == 2:
        tra_tu = input('Nhập từ cần tra:\n')
        if tra_tu in tu_dien:
            print(f'{tra_tu} có nghĩa tiếng việt là {tu_dien[tra_tu]}')
        else:
            print('Không tìm thấy từ trong từ điển')
        tiep_tuc = int(input('Tiếp tục lựa chọn? 1: Có; 0: Không\n'))
        if tiep_tuc == 1:
            continue
        break
    elif lua_chon == 3:
        tu_anh = input('Nhập từ Anh:\n')
        tu_viet = input('Nhập nghĩa tiếng Việt\n')
        tu_dien[tu_anh] = tu_viet

        # danh_ba = sorted(danh_ba.keys())
        print('Dictionary:\nTừ Anh      Nghĩa Việt')
        for i in tu_dien:
            print(f'{i}         {tu_dien[i]}')
        tiep_tuc = int(input('Tiếp tục lựa chọn? 1: Có; 0: Không\n'))
        if tiep_tuc == 1:
            continue
        break
    elif lua_chon == 4:
        tu_xoa = input('Nhập từ cần xóa:\n')
        if tu_xoa in tu_dien:
            if int(input('Bạn có thật sự muốn xóa hay không? 1: Xóa, 0: Không\n')) == 1:
                del tu_dien[tu_xoa]
                print(f'Đã xóa từ {tu_xoa} trong từ điển')
            else:
                print(f'Từ {tu_xoa} không được xóa khỏi từ điển')
        else:
            print(f'Không tìm thấy từ {tu_xoa} trong từ điển')

        # danh_ba = sorted(danh_ba.keys())
        print('Dictionary:\nTừ Anh      Nghĩa Việt')
        for i in tu_dien:
            print(f'{i}         {tu_dien[i]}')
        tiep_tuc = int(input('Tiếp tục lựa chọn? 1: Có; 0: Không\n'))
        if tiep_tuc == 1:
            continue
        break
    else:
        print('Mời chọn đúng giá trị')