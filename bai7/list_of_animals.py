list_of_animals = [animals for animals in input('Nhập và tên các con vật: ').split()]
print(f'List of animals: {list_of_animals}')
print(f'Number of animals: {len(list_of_animals)}')
animals = input('I want to find:\n')
if animals in list_of_animals:
    print(f'There is {animals} in list of anials')
else:
    print(f'There is no {animals} in list of anials')