hoa_don = {}

def tinh_tien(thanh_tien, thanh_vien):
    if thanh_vien == 1:
        return thanh_tien * 0.9
    return thanh_tien

def nhap_hoa_don():
    while True:
        ten_hang = input('Nhập tên hàng: ')
        hoa_don[ten_hang] = eval(input('Nhập đơn giá: '))
        if input('Nhập nữa không? (0/1): ') == '0':
            break
        
def main():
    nhap_hoa_don()
    # print(hoa_don)
    tong_cong = 0
    for ten_hang in hoa_don:
        tong_cong += hoa_don[ten_hang]
    print(f'Tổng cộng: {tong_cong}')
    thanh_vien = int(input('Thành viên? (0: Không / 1: Có): '))
    thanh_tien = tinh_tien(tong_cong, thanh_vien)
    print(f'Thành tiền: {thanh_tien}')

if __name__ == "__main__":
    main()