import random

memory = [
    "RESOLVE", "CHICKEN", "ADDRESS", "DESPITE",
    "REFUGEE", "DISPLAY", "PENALTY", "IMPROVE"
]

secret_password = random.choice(memory)

def compare_words(secret, guess):
    matches = 0
    for s, g in zip(secret, guess):
        if s == g:
            matches += 1
    return matches

def play_game():
    tries = 4
    print("Find the password in the computer's memory:")

    while tries > 0:
        print(f"\nEnter password: ({tries} tries remaining)")
        guess = input("> ").upper()

        if guess not in memory:
            print("Access Denied (Invalid password).")
            continue

        if guess == secret_password:
            print("A C C E S S  G R A N T E D")
            break
        else:
            matches = compare_words(secret_password, guess)
            print(f"Access Denied ({matches}/7 correct)")
            tries -= 1

    if tries == 0:
            print(f"\nOut of tries! The correct password was: {secret_password}")

play_game()