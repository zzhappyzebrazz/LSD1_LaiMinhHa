def kiem_tra_so_chan(so):
    if so == 0 or not(so % 2):
        return True
    return False

def main():
    lst = []
    lst_chan = []
    while True:
        lst.append(eval(input('Nhập vào một số: ')))
        if input('Tiếp tục nhập số? (0/1): ') == '0':
            break
    for i in lst:
        if kiem_tra_so_chan(i):
            lst_chan.append(i)
    print(f'Danh sách số đã nhập: {lst}')
    print(f'Danh sách số chẵn: {lst_chan}')
    
if __name__ == "__main__":
    main()