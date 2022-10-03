def main():
    lst = []
    while True:
        nguoi_dung_nhap = input('Người dùng nhập: ')
        if nguoi_dung_nhap:
            lst.append(nguoi_dung_nhap)
        else:
            break
    for text in lst:
        print(f'Kết quả: {text.lower()}')
    
if __name__ == "__main__":
    main()