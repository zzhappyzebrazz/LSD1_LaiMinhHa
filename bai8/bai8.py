Can = ['Canh', 'Tân', 'Nhâm', 'Quý', 'Giáp', 'Ất', 'Bính', 'Đinh', 'Mậu', 'Kỷ']
Chi = ['Thân', 'Dậu', 'Tuất', 'Hợi', 'Tý', 'Sửu', 'Dần', 'Mão', 'Thình', 'Tỵ' , 'Ngọ', 'Mùi']

def sign(x):
    if x < 0:
        return -1
    elif x > 0:
        return 1
    else:
        return 0

def nam_am_lich(nam):
    return Can[nam%10] + ' ' + Chi[nam%12]

def tinh_BMI(can_nang, chieu_cao):
    bmi = can_nang / (chieu_cao * chieu_cao)
    return bmi, danh_gia_BMI(bmi)

def danh_gia_BMI(bmi):
    if bmi < 18.5:
        return 'Gầy'
    elif bmi < 24.99:
        return 'Bình thường'
    else:
        return 'Thừa cân'

def main():
    print(sign(8))
    print(sign(-8))
    print(sign(0))
    # nam = int(input('Mời nhập năm:\n'))
    # print(f'Năm {nam} âm lịch là năm {nam_am_lich(nam)}')
    can_nang = float(input('Nhập cân nặng (kg):\n'))
    chieu_cao = float(input('Nhập chiều cao (m):\n'))
    bmi, ket_qua = tinh_BMI(can_nang, chieu_cao)
    print(f'Chỉ số BMI của bạn: {bmi}\nKết quả: {ket_qua}')

if __name__ == "__main__":
    main()