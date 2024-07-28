
def is_guess_valid(guess: str, old_guesses: list[str]) -> bool:
    return len(guess) == 1 and not (guess in old_guesses)

def wait_for_valid_guess(old_guesses: list[str]) -> str:
    guess = input('enter guess: ')

    while not is_guess_valid(guess, old_guesses):
        guess = input('enter guess: ')

    return guess