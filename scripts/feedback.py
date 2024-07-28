
def check_guess(guess: str, word: str) -> bool:
    if guess in list(word):
        print(f'"{guess}" is correct ✅')
        return True
    
    print(f'"{guess}" is incorrect ❌')
    return False

def check_win(old_guesses: list[str], word: str) -> bool:
    letters_guessed = [letter in old_guesses for letter in word]

    if all(letters_guessed):
        print('You won!!! ⭐')
        return True
    
    print(f'You have {letters_guessed.count(False)} letters left')
    return False

def check_loss(lives: int) -> bool:
    if lives <= 0:
        print("You lost 😒")
        return True
    
    print(f'You have {lives} lives left')
    return False

def show_hidden_word(old_guesses: list[str], word: str):
    hidden_word = ""

    for letter in word:
        if letter in old_guesses:
            hidden_word += letter
        else:
            hidden_word += "_"

    print(f'The word is: {hidden_word}')

def show_old_guesses(old_guesses: list[str]):
    print(", ".join(old_guesses))