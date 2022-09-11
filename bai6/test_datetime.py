# from calendar import calendar
# import time
# from datetime import datetime
import calendar 
nam = int(input("Nhập năm: "))
thang = int(input("Nhập tháng: "))
ngay_trong_thang = calendar.monthrange(nam, thang)

ngay_trong_tuan = ['Thứ hai', 'Thứ ba', 'Thứ tư', 'Thứ năm', 'Thứ sáu', 'Thứ bảy', 'Chủ nhât']

if calendar.isleap(nam):
    print(f'Năm {nam} là năm nhuận')
else:
    print(f'Năm {nam} không phải là năm nhuận')
print(f'Tháng {thang}/{nam} có {ngay_trong_thang[1]} ngày')

ngay_cuoi_cua_thang = calendar.weekday(nam, thang, ngay_trong_thang[1])

print(f'Ngày cuối cùng của tháng {thang}/{nam} là thứ {ngay_trong_tuan[ngay_cuoi_cua_thang]}')

print(f'Ngày chủ nhật đầu tiên trong tháng là ngày {1 + 6 - ngay_trong_thang[0]}')