from game_logic import play_game

def main():
    """Runs the main game loop, and ask the player if they want to play again."""
    while True:
        play_game()
        again = input("Would you like to play again? (y/n): ").lower()
        if again != "y":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
