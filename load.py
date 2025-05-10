import json
import os

INDEX_FILE = "inverted_index.json"
'''
This function is used to load the index file from the file system into the program
The function returns the inverted index
'''
def load_inverted_index():
    if os.path.exists(INDEX_FILE):
        with open(INDEX_FILE, 'r') as f:
            inverted_index = json.load(f)
        print(f"Inverted index loaded from {INDEX_FILE}")
        return inverted_index
    else:
        print(f"No file found at {INDEX_FILE}")
        return None