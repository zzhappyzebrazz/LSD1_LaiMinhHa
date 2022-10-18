import datetime
import math
import pandas
import django

def nam_toi__100_tuoi():
    ho_ten = input('Tên của bạn là gì?')
    tuoi = int(input('Bạn bao nhiêu tuổi?'))
    today = datetime.date.today()
    year = int(today.year)
    nam_toi_100_tuoi = year - tuoi + 100
    print(f'Xin chào {ho_ten}!')
    print(f'Năm bạn 100 tuổi là {nam_toi_100_tuoi}!')
    
def chan_le(so):
    if so%2:
        return False
    else:
        return True

def ban_kinh_hinh_tron(S):
    R = (S / math.pi)**0.5
    P = R * 2 * math.pi

def main():
    nam_toi__100_tuoi()
    
if __name__ == "__main__":
    main()
    