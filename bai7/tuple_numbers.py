Tuple_a = (3, 1, 2, 4)
Tuple_b = (5, 7, 6, 8)
Tuple_c = Tuple_a + Tuple_b
Tuple_d = list(Tuple_c)
Tuple_d.sort()
Tuple_d = tuple(Tuple_d)

print(f'Tuple a: {Tuple_a}')
print(f'Tuple b: {Tuple_b}')
print(f'Tuple c: {Tuple_c}')
print(f'Tuple d: {Tuple_d}')
print(f'Tuple[3] = {Tuple_d[3]}')
print(f'3 phần tử cuối cùng của tuple d {Tuple_d[-3:]}')