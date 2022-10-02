import os
import xu_ly_tap_tin

def main():
    filename = input('Nhập tên tập tin:\n')
    pwd = os.getcwd()
    fullpath = pwd + '/bai11/' + filename
    # content = xu_ly_tap_tin.read_file(fullpath)
    # print('Nội dung tập tin:')
    # print(content)
    Lines, Words, Chars = xu_ly_tap_tin.read_report_file(fullpath)
    print('-----Report: Lines/ Words/ Chars-----')
    print(f'Lines: {Lines}, Words: {Words}, Chars: {Chars}')
    
    
if __name__ == "__main__":
    main()