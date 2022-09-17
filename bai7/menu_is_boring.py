def menu_is_boring(meals):
    for i in meals:
        if meals.count(i) >= 2:
            return True
    return False
    
def main():
    meals_1 = ['Redneck Ribs', 'Prawn Star', 'San Quentin Squid', 'First Full of Pizza', 'Honky Tonk Chicken']
    meals_2 = ['Redneck Ribs', 'Prawn Star', 'Running Bear Salmon', 'Running Bear Salmon', 'Honky Tonk Chicken']
    print(menu_is_boring(meals_1))
    print(menu_is_boring(meals_2))

if __name__ == "__main__":
    main()
    