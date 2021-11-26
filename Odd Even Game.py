import random

while True:
    comp = random.randint(1, 10)

    print(" ##### WELCOME TO ODD Or EVEN GAME: ##### ")
    name = input("Enter Your Name to start the Game: ")
    choi = input("Enter the choice ODD or EVEN:\n")
    num = int(input("CHOOSE THE NUMBER FROM 1 TO 10:\n"))

    sum = comp + num

    if(choi == 'even' or choi == 'Even' or choi == 'EVEN'):
        if(sum % 2 == 0):
            print(
                f"  Computer choose : {comp}\n   {name} choose : {num}\n  Total is {sum} ")
            print(f" **{name} WON THE GAME** \n")
        else:
            print(
                f"  Computer choose : {comp}\n  {name} choose : {num}\n  Total is {sum}  ")
            print(f" **{name} LOST THE GAME** \n")

    if(choi == 'odd' or choi == 'ODD' or choi == 'Odd'):
        if(sum % 2 != 0):
            print(
                f"  Computer choose : {comp}\n   {name} choose : {num}\n  Total is {sum} ")
            print(f" **{name} WON THE GAME** \n")
        else:
            print(
                f"  Computer choose : {comp}\n   {name} choose : {num}\n   Total is {sum} ")
            print(f" **{name} LOST THE GAME** \n")
    user_choice = input("Want to Play again?(Yes/Exit)\n")
    if user_choice == 'yes' or user_choice == 'Yes' or user_choice == 'YES':
        continue
    else:
        break
