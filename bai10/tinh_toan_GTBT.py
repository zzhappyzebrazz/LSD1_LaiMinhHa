from bai9 import ham_dictionary_7

def tinhGTBT(x, y):
    A = ((5 * x - y)/(2 * x + 7 * y)) ** 0.5
    return A

def main():
    x = int(input('Nhập x:\n'))
    y = int(input('Nhập y:\n'))
    try:
        A = tinhGTBT(x, y)
    except ZeroDivisionError as er:
        print(f'Error: {er}')
    else:
        print(f'A = {A}')

    #Bài 10.2
    try:
        ham_dictionary_7.f_danh_ba()
    except ValueError as er:
        print(f'Error: {er}')
       
if __name__ == "__main__":
    main()