# list_1 = [i for i in range(10)]

# print(list_1)
# list_1[4] = 500
# print(list_1)
# del(list_1[4])
# print(list_1)

# list_1 = [1, 2, 3]
# list_2 = [4, 5, 6]
# list_3 = [7, 8, 9]

# list_1.extend(list_3)
# list_2.extend(list_1)

# list_4 = list_2
# list_4.sort(reverse=True)
# # list_4 = None
# print(list_4)

# list_animals = ['cat', 'dog', 'ant', 'mouse', 'rabbit']
# animals_upper = [animal.upper() for animal in list_animals]
# print(animals_upper)
# animals_t = [animal for animal in list_animals if 'a' in animal]
# print(animals_t)

# list_diem = [8.3, 9, 7.1, 5.0, 6, 4, 7, 2.5]
# for x in list_diem:
#     print(x)
# print(x)
# del x
# print(x)
# list_ket_qua = ['Đậu' if x >= 5.0 else 'Rớt' for x in list_diem]
# print(list_ket_qua)

tup_1 = 1,2,3,2,

print(tup_1)
list_5 = list(tup_1)
print(len(tup_1))
list_1 = [8.3, 9, 7.1, 5.0, 6, 4, 7, 2.5]

dict_1 = {
    tup_1: list_1
}
print(dict_1.get(tup_1.index(3)))