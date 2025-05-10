import build, load, find, print as print_module
import os

INVERTED_INDEX = None
NUMBER_OF_PAGES = 10
BASE_URL = "https://quotes.toscrape.com"
INDEX_FILE = "inverted_index.json"

def main():
    global INVERTED_INDEX, NUMBER_OF_PAGES
    while True:
        print("1. Build Inverted Index")
        print("2. Load Inverted Index")
        print("3. Print Inverted Index For A Word")
        print("4. Find Inverted Index For A List Of Words")
        print("5. Exit")
        args = input("Enter your choice: ").lower().split()

        if args[0] == '1' or args[0] == 'build':
            NUMBER_OF_PAGES = build.crawl_and_build_index(BASE_URL, INDEX_FILE)
        elif args[0] == '2' or args[0] == 'load':
            INVERTED_INDEX = load.load_inverted_index()
        elif args[0] == '3' or args[0] == 'print':
            if INVERTED_INDEX is None:
                print("Inverted index is not loaded")
            elif len(args) < 2 or len(args) > 2:
                print("Incorrect number of arguments")
            else:
                print_module.print_inverted_index(INVERTED_INDEX, args[1])
        elif args[0] == '4' or args[0] == 'find':
            if INVERTED_INDEX is None:
                print("Inverted index is not loaded")
            elif len(args) < 2:
                print("Provide at least one word")
            else:
                words = args[1:]
                ranked_pages = find.find_ranked_pages(INVERTED_INDEX, words, NUMBER_OF_PAGES)
        elif args[0] == '5' or args[0] == 'exit':
            print("Exiting")
            break

if __name__ == "__main__":
    main()