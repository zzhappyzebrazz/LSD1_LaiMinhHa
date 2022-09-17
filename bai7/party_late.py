import math


def party_late (arrivals, name):
    so_khach = len(arrivals)
    # print(arrivals[math.floor(so_khach/2) : so_khach - 1])
    if name in arrivals[math.floor(so_khach/2) : so_khach - 1]:
        return True
    return False
    
def main():
    arrivals = ['Adela', 'Fleda', 'Owen', 'May', 'Mona', 'Gilbert', 'Fort']
    print(party_late(arrivals, 'Gilbert'))
    print(party_late(arrivals, 'Ford'))
    print(party_late(arrivals, 'Mona'))

if __name__ == "__main__":
    main()
    