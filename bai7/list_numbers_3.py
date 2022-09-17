list_numbers = [74, 74, 72, 72, 73, 69, 69, 71, 76, 71]
print('list_number: ',list_numbers)
so_phan_tu = len(list_numbers)
list_met = [x * 0.0254 for x in list_numbers if x]
print('list_met: ', list_met)

print(f'3 chiều cao đầu tiên: {list_met[0]:.2f}m, {list_met[1]:.2f}m, {list_met[2]:.2f}m')
print(f'3 chiều cao cuối cùng: {list_met[so_phan_tu -3]:.2f}m, {list_met[so_phan_tu -2]:.2f}m, {list_met[so_phan_tu -1]:.2f}m')
print(f'Chiều cao trung bình: {sum(list_met)/so_phan_tu:.2f}m')
list_met.sort();
print(f'Chiều cao theo giá trị tăng dần: ', end="")
for i in range(so_phan_tu):
    if i == so_phan_tu -1:
        print('%.2fm' %list_met[i])
    else:
        print('%.2fm' %list_met[i], end=', ')
list_met.reverse()
print(f'Chiều cao theo giá trị giảm dần: ', end="")
for i in range(so_phan_tu):
    if i == so_phan_tu -1:
        print('%.2fm' %list_met[i])
    else:
        print('%.2fm' %list_met[i], end=', ')