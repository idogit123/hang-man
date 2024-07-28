from scripts.read_words import get_word_from_file
from scripts.validator import wait_for_valid_guess
from scripts.feedback import *


def main():
    old_guesses: list[str] = []
    is_over = False
    lives = 5

    # select secret word
    words_file = input('enter words file path: ')
    word_index = int(input('enter word index: '))
    word = get_word_from_file(words_file, word_index)
    
    # game loop
    while not is_over: 
        guess = wait_for_valid_guess(old_guesses)
        old_guesses.append(guess)

        if check_guess(guess, word):
            is_over = check_win(old_guesses, word)

        else:
            lives -= 1
            is_over = check_loss(lives)

        show_hidden_word(old_guesses, word)
        show_old_guesses(old_guesses)
            
main()