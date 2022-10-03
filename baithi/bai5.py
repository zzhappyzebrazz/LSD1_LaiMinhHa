import bai2
import os
import codecs

def main():
    bai2.nhap_hoa_don()
    # print(hoa_don)
    tong_cong = 0
    for ten_hang in bai2.hoa_don:
        tong_cong += bai2.hoa_don[ten_hang]
    print(f'Tổng cộng: {tong_cong}')
    thanh_vien = int(input('Thành viên? (0: Không / 1: Có): '))
    thanh_tien = bai2.tinh_tien(tong_cong, thanh_vien)
    print(f'Thành tiền: {thanh_tien}')

    path = os.getcwd()
    filename = path + '/hoadon.txt'
    if not os.path.isfile(filename):
        with open(filename, 'w'):
            pass

    s = '--- HÓA ĐƠN ---\n'
    for ten_hang in bai2.hoa_don:
        s += ten_hang + ': ' + str(bai2.hoa_don[ten_hang]) + '\n'

    s += '--------------------\n'
    s += 'Tổng: ' + str(tong_cong) + '\n'
    if thanh_vien == 1:
        s += 'Thành viên: Có\n'
    else:
        s += 'Thành viên: Không\n'
    s += '--------------------\n'
    s += 'Tiền thanh toán: ' + str(thanh_tien)
    f = codecs.open(filename, 'w', 'utf-8')
    f.write(s)
    f.close()
    
if __name__ == "__main__":
    main()