import calendar
import time
from datetime import datetime
import math

def timGiaTriMaxMin():
    userData = [float (x) for x in input("Nhập dãy số cần tìm Max và Min\n").split()]
    maxNumber = max(userData)
    minNumber = min(userData)
    print(f'Số max là {maxNumber}, số min là {minNumber}')

def timGiaTriTuyetDoi():
    userData = float(input("Nhập số cần tìm giá trị tuyệt đối\n"))
    result = abs(userData)
    print(f"Giá trị tuyệt đối của số cần tìm {result}")

def tinhPhuongTrinhS1():
    n = float(input("Nhập giá trị n\n"))
    x = float(input(f"Phương trình: S = (x^2 + 1)^{n} với x = "))
    S1 = pow((pow(x, 2) + 1), n)
    print(f'Kết quả S = {S1}')

def tinhPhuongTrinhS2():
    n = float(input("Nhập giá trị n\n"))
    x = float(input(f"Phương trình: S = (x^2 + x + 1)^{n} + (x^2 - x + 1)^{n} với x = "))
    S2 = pow((pow(x, 2) + x + 1), n) + pow((pow(x, 2) - x + 1), n)
    print(f'Kết quả S = {S2}') 

def kiemTraZIPcode():
    zip = input("Nhập mã zip code\n")
    if len(zip) == 6 and zip.isnumeric():
        print("Mã zip hợp lệ")
    else:
        print("Mã zip không hợp lệ")

def giaiPhuongTrinhBac2():
    a , b, c = [float (x) for x in input("Nhập 3 tham số cho phương trình bậc 2 ax^2 + bx + c = 0").split()]
    if a:
        delta = b**2 - 4 * a * c
        if delta > 0:
            print(f'Phương trình có 2 nghiệm phân biệt x1 = {(-b + math.sprt(delta))/(2 * a)}, x2 = {(-b - math.sprt(delta))/(2 * a)}')
        elif delta < 0:
            print("Phương trình vô nghiệm")
        else:
            print(f'Phương trình có 2 nghiệm kép x1 = x2 = x0 = {-b / (2 * a)}')

    else:
        if b == 0:
            print("Phương trình vô nghiệm")
            if c == 0:
                print("Phương trình vô số nghiệm")
        else:
            print(f'Phương trình có 1 nghiệm là x = {-c/b}')

def word_search(doc_list, keyword):
    result = {}
    for x in range(len(doc_list)):
        split_doc = doc_list[x].split()
        for y in split_doc:
            '''tách các word thành letter và check nếu tất cả letter đều là alphabet và number thì giữ lại và join
            example: getVals =  "123abcjw:, .@! eiw" = ['1', '2', ... , 'a' , 'b', 'c', ... , '.', '@', '!' ,..., 'e', 'i', 'w'] -Chuỗi original
            getVals = ['1','2','3','a','b','c','j','w','e','i','w'] -Chuỗi sau khi tách các ký tự đặc biệt
            getVals = "123abcjweiw" -Chuỗi sau khi join
            '''
            getVals = list([val for val in y if val.isalpha() or val.isnumeric()])
            getVals = "".join(getVals)
            if getVals.lower() == keyword:
                result[x] = doc_list[x]
    return result

def multi_word_search(doc_list, keywords):
    resultDict = {}
    for keyword in keywords:
        resultList = []
        for x in range(len(doc_list)):
            split_doc = doc_list[x].split()
            for y in split_doc:
                '''tách các word thành letter và check nếu tất cả letter đều là alphabet và number thì giữ lại và join
                example: getVals =  "123abcjw:, .@! eiw" = ['1', '2', ... , 'a' , 'b', 'c', ... , '.', '@', '!' ,..., 'e', 'i', 'w']
                getVals = ['1','2','3','a','b','c','j','w','e','i','w']
                getVals = "123abcjweiw"
                '''
                getVals = list([val for val in y if val.isalpha() or val.isnumeric()])
                getVals = "".join(getVals)
                if getVals.lower() == keyword:
                    resultList.append(x)
                    resultDict[keyword] = resultList
    return resultDict

# def word_searchV1(doc_list, keyword):
#     result = []
#     for x in range(len(doc_list)):
#         string = doc_list[x].strip([".",",","!","?"])
#         for y in string
#         if string.find(keyword) != -1:
#             result.append(x)
#     return result

def best_items(racers):
    result = {}
    for x in range(len(racers)):
        player = racers[x]
        if player['finish'] == 1:
            result[x] = len(player['items'])
    return result

def xu_ly_chuoi():
    count = 0
    s = input("Nhập chuỗi s:\n")
    s_sub = input("Nhập chuỗi con s_sub:\n")
    s_find = input("Nhập chuỗi tìm s_find:\n")
    s_replace = input("Nhập chuỗi thay thế s_replace:\n")

    print(s)
    s = s.strip()
    print(f'Chuỗi sau khi loại bỏ khoảng trắng đầu và cuối chuỗi {s}')
    s = s.capitalize()
    print(f'Chuỗi viết hoa ký tự đầu: {s}')
    chuoi_cat = s.split()
    for x in range(len(chuoi_cat)):
        if chuoi_cat[x].find(s_sub) != -1:
            count += 1
        if chuoi_cat[x] == s_find:
            chuoi_cat[x] = s_replace
    chuoi_ket_qua = ' '.join(chuoi_cat)
    print(f'Số lần {s_sub} xuất hiện trong {s}: {count}')
    print(f'Chuỗi {s} sau khi tìm kiếm và thay thế: {chuoi_ket_qua}')

def su_dung_Datetimes():
    ngay, thang, nam = [int (x) for x in input("Nhập ngày tháng năm cần xử lý\n").split()]
    ngay_trong_tuan = ['Thứ hai', 'Thứ ba', 'Thứ tư', 'Thứ năm', 'Thứ sáu', 'Thứ 7', 'Chủ nhật']
    if datetime(nam, thang, ngay):
        user_data = datetime(nam, thang, ngay)
        print(f"Ngày tháng năm đã nhập là {user_data.strftime('%d-%m-%Y')}")
        if calendar.isleap(nam):
            print(f'Năm đã nhập {nam} là năm nhuận')
        else:
            print(f'Năm đã nhập {nam} không là năm nhuận')
        ngay_can_tim = calendar.weekday(nam, thang, ngay)
        print(f'Ngày {ngay}/{thang}/{nam} đã nhập vào là {ngay_trong_tuan[ngay_can_tim]}')
        so_ngay_trong_thang = calendar.monthrange(nam, thang)[1]
        print(f'Tháng {thang} có {so_ngay_trong_thang} ngày')
    else:
        print("Chương trình Error")



def main():
    # timGiaTriMaxMin()
    # timGiaTriTuyetDoi()
    # tinhPhuongTrinhS2()
    # kiemTraZIPcode()
    doc_list = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"]
    doc_list2 = ["The Learn Python./\| Challenge@!# Casino /9635***.", "They bought a car", "Casinoville is in Ittaly", "They bought a car and a casino"]
    sample = [
        {'name' : 'Peach', 'items' : ['green shell', 'banana', 'green shell',], 'finish': 3},
        {'name' : 'Bowser', 'items' : ['green shell',], 'finish': 1},
        {'name' : None, 'items' : ['mushroom',], 'finish': 2}, 
        {'name' : 'Toad', 'items' : ['green shell', 'mushroom',], 'finish': 1},
    ]
    keywords = ['casino', 'they']
    # xu_ly_chuoi()
    su_dung_Datetimes()

    
if __name__ == "__main__":
    main()