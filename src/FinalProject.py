import random
import pygame

def display(result):
    pygame.init()
    pygame.display.set_caption("Game Result")
    resolution = (800, 600)
    screen = pygame.display.set_mode(resolution)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        black = pygame.Color(0, 0, 0)
        screen.fill(black)
        if result == "win":
            # Display win message
            pass
        else:
            # Display lose message
            pass
        pygame.display.flip()
    pygame.quit()

    
def get_character_names():
    with open('character_names.txt', 'r') as character_names:
        file_names = list(character_names)
    return file_names
#needs code for not having an extra dash/ space at the end of the guessing word in terminal.
def case():
    chosen_name = chosen_name.lower()
    guess = guess.lower()
    #if guess not in chosen_name:

def main():
    character_names = get_character_names()
    chosen_name = random.choice(character_names).strip().lower()
    first_char = chosen_name[0]
    print("Guess a letter")
    #if guess.lower() not in chosen_name.lower():
    guesses = ''
    turns = len(chosen_name) + 1
    while turns > 0:
        failed = 0
        win_str = ''
        for char in chosen_name:
            if char in guesses:
                win_str += char + ' '
            #terminal guessing word horizontal.
            else:
                win_str += '_ '
                failed += 1
        if win_str[0] != "_":
            win_str = first_char.upper() + win_str[1:]
        print(win_str)
        if failed == 0:
            print("You win")
            print("The Character is: ", chosen_name)
            display("win")
            break
        print()
        guess = input("Guess a letter:").lower()
        guesses += guess
        if guess not in chosen_name:
            turns -= 1
            print('Wrong')
            print("You have", + turns, 'more guesses')
            if turns == 0:
                print("You Loose")
                print("The correct answer was:", chosen_name)
                display("lose")
        

if __name__ == "__main__":
    main()