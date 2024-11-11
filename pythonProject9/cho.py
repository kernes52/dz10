import random, sys

JAPANESE_NUMBERS = {1: 'ICI', 2: 'NI', 3: 'SAN',
                    4: 'SHI', 5: 'GO', 6: 'ROKU'}

purse = 5000

while True:
    print("You have", purse, "mon. How much do you bet? (or Quit)")
    while True:
        pot = input("> ")
        if pot.upper() == "Quit":
            print("Thanks for playig!")
            sys.exit()
        elif not pot.isdecimal():
            print("Please enter a number.")
        elif int(pot) > purse:
            print("You don't have enough to make that bet.")
        else:
            pot = int(pot)
            break

    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

    print("The dealer swirls the cup and you hear the rattle of dice.")
    print("the dealer slams the cup on the floor, still covering the")
    print("dice and asks for your bet.")
    print()
    print('    CHO (even) or HAN (odd)?')

    while True:
        bet = input("> ").upper()
        if bet != 'CHO' and bet != 'HAN':
            print("Please enter either 'CHO' or 'HAN'.")
            continue
        else:
            break

    print("The dealer swirls the cup and you hear the rattle of dice.")
    print("  ", JAPANESE_NUMBERS[dice1], "-", JAPANESE_NUMBERS[dice2])
    print("   ", dice1, "-", dice2)

    rollsEven = (dice1 + dice2) % 2 == 0
    if rollsEven:
        correctbet = 'CHO'
    else:
        correctbet = 'HAN'

    playerWon = bet == correctbet

    if playerWon:
        print("You won! You take", pot, "mon.")
        purse = purse + pot
        print("The house collects a", pot // 10, "mon fee.")
        purse = purse - (pot // 10)
    else:
        purse = purse - pot
        print("you lost!")

    if purse == 0:
        print("you have run out of money!")
        print("Thanks for playing!")
        sys.exit()