import build
from collections import defaultdict
import math

'''
This function is used to find pages that contain a set of words. The pages are
ranked based on term frequency.
The funciton returns the ranked pages
'''
def find_ranked_pages(inverted_index, words, number_of_pages):
    normalized_words = [build.normalize_word(word) for word in words]

    index_for_specific_words = defaultdict(lambda: defaultdict(int))
    for word in normalized_words:
        if word in inverted_index:
            for url, count in inverted_index[word].items():
                index_for_specific_words[url][word] += count
        else:
            print(f'No occurrences of "{word}" found')
            return None
        
    idf_word = defaultdict(int)
    for word in normalized_words:
        pages = len(inverted_index[word].keys())
        idf_word[word] = math.log(number_of_pages / pages)

    # common pages
    page_ranks = []
    for url, word_counts in index_for_specific_words.items():
        # Check if the page contains all the words
        tf_idf = 0
        total_count = 0
        all_words_present = True
        for word in normalized_words:
            if word not in word_counts:
                all_words_present = False
                break
            tf_idf += word_counts[word] * idf_word[word]
            total_count += word_counts[word]
        if all_words_present:
            page_ranks.append((url, tf_idf, total_count))

    # Sort pages by total count in descending order
    page_ranks.sort(key=lambda x: x[1], reverse=True)

    print("Ranked pages:")
    for url, tf_idf, total_count in page_ranks:
        print(f"  URL: {url}, Total Count: {total_count}")

    return page_ranks
