import random

TOTAL_ROUNDS = 3
CHOICES = {"r": "Rock", "p": "Paper", "s": "Scissors"}

# Each key beats its value
BEATS = {"Rock": "Scissors", "Scissors": "Paper", "Paper": "Rock"}


def show_instructions():
    print("=" * 42)
    print("      ROCK - PAPER - SCISSORS GAME")
    print("=" * 42)
    print("Rules:")
    print(f"  * The game has {TOTAL_ROUNDS} rounds.")
    print("  * Rock beats Scissors")
    print("  * Scissors beat Paper")
    print("  * Paper beats Rock")
    print(f"  * The player with the highest score after")
    print(f"    {TOTAL_ROUNDS} rounds wins the game!")
    print("=" * 42 + "\n")


def get_user_choice():
    """Keep asking until the user enters R, P or S."""
    while True:
        ch = input("Enter your choice - (R)ock, (P)aper or (S)cissors: ").strip().lower()
        if ch in CHOICES:
            return CHOICES[ch]
        print("  Invalid choice! Please type R, P or S.")


def decide_winner(user, comp):
    """Return 1 if user wins, -1 if computer wins, 0 if tie."""
    if user == comp:
        return 0
    return 1 if BEATS[user] == comp else -1


def play_game():
    user_score = 0
    comp_score = 0

    for round_no in range(1, TOTAL_ROUNDS + 1):
        print(f"--- Round {round_no} of {TOTAL_ROUNDS} ---")

        user = get_user_choice()
        comp = random.choice(list(CHOICES.values()))

        print(f"\nYou chose      : {user}")
        print(f"Computer chose : {comp}")

        result = decide_winner(user, comp)
        if result == 1:
            user_score += 1
            print("Result         : You win this round!")
        elif result == -1:
            comp_score += 1
            print("Result         : Computer wins this round!")
        else:
            print("Result         : It's a tie!")

        print(f"Score -> You: {user_score} | Computer: {comp_score}\n")

    print("=" * 42)
    print("            FINAL RESULT")
    print("=" * 42)
    print(f"Your score     : {user_score}")
    print(f"Computer score : {comp_score}")

    if user_score > comp_score:
        print("\nCongratulations! You won the game!")
    elif comp_score > user_score:
        print("\nComputer won the game. Better luck next time!")
    else:
        print("\nThe game is a draw!")
    print("=" * 42)


def main():
    show_instructions()
    while True:
        play_game()
        again = input("\nDo you want to play again? (y/n): ").strip().lower()
        print()
        if again != "y":
            break
    print("Thanks for playing. Goodbye!")


if __name__ == "__main__":
    main()