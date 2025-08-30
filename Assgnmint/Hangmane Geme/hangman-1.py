import random
import sys
import os


HANGMAN_PICS = [
    """
     +---+
         |
         |
         |
        ===""",
    """
     +---+
     O   |
         |
         |
        ===""",
    """
     +---+
     O   |
     |   |
         |
        ===""",
    """
     +---+
     O   |
    /|   |
         |
        ===""",
    """
     +---+
     O   |
    /|\\  |
         |
        ===""",
    """
     +---+
     O   |
    /|\\  |
    /    |
        ===""",
    """
     +---+
     O   |
    /|\\  |
    / \\  |
        ==="""
]

DEFAULT_WORDS = [
    "python", "hangman", "computer", "programming", "developer",
    "algorithm", "function", "variable", "terminal", "keyboard",
    "internet", "package", "module", "string", "integer"
]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def load_words_from_file(path):
    """Load words from a text file (one word per line). If fails, use default words."""
    try:
        with open(path, encoding='utf-8') as f:
            words = [line.strip() for line in f if line.strip()]
            return words if words else DEFAULT_WORDS
    except Exception:
        return DEFAULT_WORDS

def choose_word(words, min_len=1, max_len=100):
    suitable = [w for w in words if min_len <= len(w) <= max_len]
    if not suitable:
        suitable = words
    return random.choice(suitable).lower()

def display_state(missed_letters, correct_letters, secret_word):
    clear_screen()
    print(HANGMAN_PICS[len(missed_letters)])
    print()
    print("Missed letters:", " ".join(sorted(missed_letters)) if missed_letters else "(none)")
    print()
    displayed = [ch if ch in correct_letters else '_' for ch in secret_word]
    print("Word:", " ".join(displayed))
    print()

def get_guess(already_guessed):
    while True:
        guess = input("Guess a letter or the whole word: ").strip().lower()
        if not guess:
            print("Please enter a letter or word.")
            continue
        if len(guess) == 1:
            if not guess.isalpha():
                print("Please enter a valid letter.")
                continue
            if guess in already_guessed:
                print("You already guessed that letter. Try another.")
                continue
        return guess

def play_game(words):
    print("Choose difficulty: (1) Easy  (2) Medium  (3) Hard  (4) Random")
    level = input("Level [1-4] (default 4): ").strip()
    if level == '1':
        min_len, max_len = 3, 6
    elif level == '2':
        min_len, max_len = 4, 8
    elif level == '3':
        min_len, max_len = 6, 100
    else:
        min_len, max_len = 1, 100

    secret_word = choose_word(words, min_len=min_len, max_len=max_len)
    missed_letters = set()
    correct_letters = set()
    all_guessed = set()
    max_misses = len(HANGMAN_PICS) - 1

    while True:
        display_state(missed_letters, correct_letters, secret_word)

        if set(secret_word) <= correct_letters:
            print("Congratulations! You won. The word was:", secret_word)
            return True
        if len(missed_letters) >= max_misses:
            print("You lost! Out of attempts. The word was:", secret_word)
            return False

        guess = get_guess(all_guessed)

        if len(guess) > 1: 
            if guess == secret_word:
                correct_letters.update(secret_word)
                display_state(missed_letters, correct_letters, secret_word)
                print("Amazing! You guessed the word correctly.")
                return True
            else:
                missed_letters.add(guess)
                all_guessed.add(guess)
                print("Wrong — that’s not the word.")
                input("Press Enter to continue...")
                continue

        letter = guess
        all_guessed.add(letter)
        if letter in secret_word:
            correct_letters.add(letter)
            print(f"Good! The letter '{letter}' is in the word.")
        else:
            missed_letters.add(letter)
            print(f"Sorry! The letter '{letter}' is not in the word.")
        input("Press Enter to continue...")

def main():
    words_file = sys.argv[1] if len(sys.argv) > 1 else None
    words = load_words_from_file(words_file) if words_file else DEFAULT_WORDS

    clear_screen()
    print("=== Hangman Game ===")
    print("Instructions: Guess letters to reveal the word. You can also try guessing the whole word.")
    print("You can provide a word file: python3 hangman.py words.txt")
    input("Press Enter to start...")

    wins = 0
    losses = 0
    while True:
        won = play_game(words)
        if won:
            wins += 1
        else:
            losses += 1

        print(f"\nCurrent Score — Wins: {wins} | Losses: {losses}")
        again = input("Play again? (y/n): ").strip().lower()
        if not again or again[0] != 'y':
            print("Thanks for playing! Goodbye.")
            break

if __name__ == "__main__":
    main()
