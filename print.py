import build


# This function prints the inverted index for a word
def print_inverted_index(inverted_index, word):
    normalized_word = build.normalize_word(word)
    if normalized_word in inverted_index:
        for url, count in inverted_index[normalized_word].items():
            print(f"  URL: {url}, Count: {count}")
    else:
        print(f'No occurrences of "{word}" found')