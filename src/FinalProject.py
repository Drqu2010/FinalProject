import random


def list():
    with open('character_names.txt', 'r') as character_names:
        file_names = list(character_names)
    print(random.choice(file_names), end='')
    

def main():
    list = random.choice(character_names)
    print("Guess a letter")
    guesses = ''
    turns = 12
    while turns > 0:
        failed = 0
        for char in list:
            if char in guesses:
                print(char, end='')
            else:
                print('_')
                failed += 1
        if failed == 0:
            print("You win")
            print("The Character is: ", list)
            break
        print()
        guess = input("Guess a letter:")
        guesses += guess
        if guess not in list:
            turns -= 1
            print('Wrong')
            print("You have", + turns, 'more guesses')
            if turns == 0:
                print("You Loose")

if __name__ == "__main__":
    main()