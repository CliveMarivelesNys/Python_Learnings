import random
import string


def generate_random_letters():
    return ''.join(random.choice(string.ascii_uppercase) for _ in range(3))


def compare_guesses(random_letters, guess):
    result = []
    for r, g in zip(random_letters, guess):
        if r == g:
            result.append(r)
        else:
            result.append('_')
    return ' '.join(result)


def guess_interface():
    score = 10
    random_letters = generate_random_letters()

    print(
        f"Random 3 letter combination: {random_letters}")
    print("Random 3 letter known: _ _ _")

    while score > 0:
        guess = input("User guess 3 letter combination: ").upper()

        if guess == random_letters:
            print("Correct Guess")
            print(f"Score: {score}")
            break
        else:
            score -= 1
            known_letters = compare_guesses(random_letters, guess)
            print(f"Random 3 letter known: {known_letters}")
            print(f"Score: {score}")

    if score == 0:
        print("Game Over")
        print(f"Score: {score}")

