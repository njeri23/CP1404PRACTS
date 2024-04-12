def count_word_occurrences(text):
    words = text.split()
    word_counts = {}

    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1

    return word_counts

def print_word_counts(word_counts):
    max_word_length = max(len(word) for word in word_counts)

    sorted_word_counts = sorted(word_counts.items())

    for word, count in sorted_word_counts:
        print(f"{word:{max_word_length}} : {count}")

def main():
    text = input("Enter a string: ")

    word_counts = count_word_occurrences(text)

    print_word_counts(word_counts)

if __name__ == "__main__":
    main()
