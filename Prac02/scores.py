from random import random


def determine_score_status(score):
    """
    Determines the status of the score
    """
    if score < 0 or score > 100:
        return "Invalid score"
    elif score > 90:
        return "Excellent"
    elif score > 50:
        return "Passable"
    else:
        return "Bad"


def main():
    score = float(input("Enter your score:"))
    result = determine_score_status(score)
    print(result)

    # Generating a random score
    random_score = random.randint(0, 100)
    random_result = determine_score_status(random_score)
    print(f"Random score ({random_score}):{random_result}")

    if __name__ == '__main__':
        main()
