import random

MIN_NUM = 1
MAX_NUM = 45
NUM_NUMBERS_PER_QUICK_PICK = 6
NUM_QUICK_PICKS = int(input("How many quick picks? "))

def generate_quick_pick():
    """Generate a quick pick."""
    quick_pick = []
    while len(quick_pick) < NUM_NUMBERS_PER_QUICK_PICK:
        number = random.randint(MIN_NUM, MAX_NUM)
        if number not in quick_pick:
            quick_pick.append(number)
    quick_pick.sort()
    return quick_pick

def main():
    """Generate quick picks."""
    for _ in range(NUM_QUICK_PICKS):
        quick_pick = generate_quick_pick()
        print(" ".join(f"{number:2}" for number in quick_pick))

if __name__ == "__main__":
    main()
