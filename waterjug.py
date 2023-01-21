# Water Jug Riddle


def main():
    print("You have a 3 gallon and 5 gallon water jug. Your task is to measure 4 gallons...")
    five_gal = 0
    three_gal = 0
    while True:
        count = int
        print("\nAvailable Commands : ")
        print("'3 to 5', '5 to 3', 'empty 5', 'empty 3', 'empty all'")
        print("'fill 3', 'fill 5'")
        print(f'\nJug of 3 gal has {three_gal} in it. ')
        print(f'{"[x]" * three_gal}')
        print(f'Jug of 5 has {five_gal} in it. ')
        print(f'{"[x]" * five_gal}')

        user_input = input("\nMake your Selection : ")
        if user_input == '3 to 5':
            five_gal = five_gal + three_gal
            if five_gal > 5:
                three_gal = five_gal - 5
                five_gal = 5
            else:
                three_gal = 0
        elif user_input == '5 to 3':
            three_gal = three_gal + five_gal
            if three_gal > 3:
                five_gal = three_gal - 3
                three_gal = 3
            else:
                five_gal = 0
        elif user_input == 'empty 5':
            five_gal = 0
        elif user_input == 'empty 3':
            three_gal = 0
        elif user_input == 'empty all':
            five_gal = 0
            three_gal = 0
        elif user_input == 'fill 5':
            five_gal = 5
        elif user_input == 'fill 3':
            three_gal = 3
        else:
            print("Not a valid command")
        if five_gal == 4:
            print('You have isolated 4 gallons!')
            print(f'\nJug of 3 gal has {three_gal} in it. ')
            print(f'{"[x]" * three_gal}')
            print(f'Jug of 5 has {five_gal} in it. ')
            print(f'{"[x]" * five_gal}')
            break


if __name__ == "__main__":
    main()
