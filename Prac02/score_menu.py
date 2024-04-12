def get_valid_score():
    score: int = -1  # Initialize score to an invalid value
    while not (0 <= score <= 100):
        try:
         score = int(input("Enter a score (0-100): "))
        if not 0 <= score <= 100:
         print("Score must be between 0 and 100, Inclusive")
        print("Invalid input. Please enter a valid integer")
        return score

def print_result(score):

    pass

def show_stars(score):
    print("*" * score)

def main():
    score = get_valid_score()
    choice = ''

    while choice != 'Q':
        print("\nMENU:")
        print("(G)et a valid score")
        print("(P)rint result")
        print("(S)how stars")
        print("(Q)uit")

        choice = input("Enter your choice: ").strip().upper()
        if choice == 'G':
            score = get_valid_score()
        elif choice == 'P':
            print_result(score)
        elif choice == 'S':
            show_stars(score)
        elif choice == 'Q':
            print("Farewell!")
        else:
            print("Invalid choice. Please enter G, P, S,Q.")

if __name__ == "__main__":
    main()
