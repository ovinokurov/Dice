import random

def dice_game():
    # ask the player to roll the dice
    input("Press Enter to roll the dice...")
    
    # generate random numbers between 1 and 6 for two dice
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

    print('Dice 1')
    draw_dice_cube(dice1)
    print('Dice 2')
    draw_dice_cube(dice2)

    # calculate the sum of the dice rolls
    total = dice1 + dice2
    
    # display the results to the player
    print("You rolled a", dice1, "and a", dice2, "for a total of", total)
    
    # determine if the player won or lost
    if total == 7 or total == 11:
        print("Congratulations! You win!")
    elif total == 2 or total == 3 or total == 12:
        print("Sorry, you lose.")
    else:
        print("Roll again. You need to roll a", total, "to win.")
        
        # keep rolling until the player wins or loses
        while True:
            input("Press Enter to roll the dice...")
            dice1 = random.randint(1, 6)
            dice2 = random.randint(1, 6)

            print('Dice 1')
            draw_dice_cube(dice1)
            print('Dice 2')
            draw_dice_cube(dice2)
            

            new_total = dice1 + dice2
            
            print("You rolled a", dice1, "and a", dice2, "for a total of", new_total)
            if new_total == total:
                print("Congratulations! You win!")
                break
            elif new_total == 7:
                print("Sorry, you lose.")
                break

def draw_dice_cube(number):
    if number == 1:
        print("+-------+")
        print("|       |")
        print("|   •   |")
        print("|       |")
        print("+-------+")
    elif number == 2:
        print("+-------+")
        print("| •     |")
        print("|       |")
        print("|     • |")
        print("+-------+")
    elif number == 3:
        print("+-------+")
        print("| •     |")
        print("|   •   |")
        print("|     • |")
        print("+-------+")
    elif number == 4:
        print("+-------+")
        print("| •   • |")
        print("|       |")
        print("| •   • |")
        print("+-------+")
    elif number == 5:
        print("+-------+")
        print("| •   • |")
        print("|   •   |")
        print("| •   • |")
        print("+-------+")
    elif number == 6:
        print("+-------+")
        print("| •   • |")
        print("| •   • |")
        print("| •   • |")
        print("+-------+")

def draw_two_dice_cube(number1, number2):
    dice1 = draw_dice_cube(number1)
    dice2 = draw_dice_cube(number2)
    print(dice1 + "   " + dice2)

# play the dice game
dice_game()
