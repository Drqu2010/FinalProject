import random
import pygame
from PIL import Image
import sys

def winner(screen):
    image = Image.open('YouWin.jpg')
    new_image = image.resize((600, 600))
    image.show()

def lose(screen):
    image = Image.open('YouLose.jpg')
    new_image = image.resize((600, 600))
    new_image.show()

def display(result):
    pygame.init()
    pygame.display.set_caption("Game Result")
    resloution = (600, 600)
    screen = pygame.display.set_mode(resloution)
    if result == "win":
        win_image = pygame.image.load('YouWin.jpg')
        screen.blit(win_image, (0, 0))
    elif result == "lose":
        lose_image = pygame.image.load('YouLose.jpg')
        screen.blit(lose_image, (0, 0))
    pygame.display.flip()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()
    sys.exit()
   
    
def get_character_names():
    with open('character_names.txt', 'r') as character_names:
        file_names = list(character_names)
    return file_names

def case():
    chosen_name = chosen_name.lower()
    guess = guess.lower()

def main():
    pygame.init()
    #screen = pygame.display.set_mode((800, 600))
    character_names = get_character_names()
    chosen_name = random.choice(character_names).strip().lower()
    first_char = chosen_name[0]
    print("Guess a letter")
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
           # winner(screen)
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
               # lose(screen)
                print("The correct answer was:", chosen_name)
                display("lose")
        

if __name__ == "__main__":
    main()