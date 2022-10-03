def tinh_tien(so_tien, thanh_vien):
    if thanh_vien == 1:
        return so_tien * 0.9
    return so_tien

def main():
    ten_hang = input('Nhập tên hàng: ')
    don_gia = float(input('Nhập đơn giá: '))
    if don_gia < 0:
        print('Số tiền không hợp lệ')
    else:
        thanh_vien = int(input('Thành viên? (0: Không / 1: Có): '))
        thanh_tien = tinh_tien(don_gia, thanh_vien)
        print(f'Thành tiền: {thanh_tien}')    
    
if __name__ == "__main__":
    main()