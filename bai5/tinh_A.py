n = int(input('Nhập n:\n'))
x = int(input('Nhập x:\n'))
A = (x * x + x + 1) ** n + (x * x - x + 1) ** n
print(f'A = (x^2 + x + 1)^n + (x^2 - x + 1)^n = {A}')