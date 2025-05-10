import build
from collections import defaultdict

'''
This function is used to find pages that contain a set of words. The pages are
ranked based on term frequency.
The funciton returns the ranked pages
'''
def find_ranked_pages(inverted_index, words):
    normalized_words = [build.normalize_word(word) for word in words]

    index_for_specific_words = defaultdict(lambda: defaultdict(int))
    for word in normalized_words:
        if word in inverted_index:
            for url, count in inverted_index[word].items():
                index_for_specific_words[url][word] += count
        else:
            print(f'No occurrences of "{word}" found')
            return None
    
    # common pages
    page_ranks = []
    for url, word_counts in index_for_specific_words.items():
        # Check if the page contains all the words
        if all(word_counts.get(word, 0) > 0 for word in normalized_words):
            total_count = sum(word_counts.values())
            page_ranks.append((url, total_count))
    
    # Sort pages by total count in descending order
    page_ranks.sort(key=lambda x: x[1], reverse=True)

    print("Ranked pages:")
    for url, count in page_ranks:
        print(f"  URL: {url}, Total Count: {count}")

    return page_ranks
