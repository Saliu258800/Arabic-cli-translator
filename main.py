import json
import os

VERSION = "v2.0.0"

def main():
    print(f"Mini English To Arabic App {VERSION}")

    # Load both word groups
    def_article = load_json("/definite_article.json")
    indef_article = load_json("/indefinite_article.json")

    # User input
    word = get_word()

    if word in def_article:
        print("Translations (Definite Article):")
        for translation in def_article[word]:
            print(" -", translation)
    elif word in indef_article:
        print("Translations (Indefinite Article):")
        for translation in indef_article[word]:
            print(" -", translation)
    else:
        print("Word not found.")

def get_path(file):
    return "./Arabic" + file

def load_json(path):
    with open(get_path(path), "r", encoding='utf-8') as f:
        return json.load(f)

def get_word():
    return input("Enter the word to translate: ").lower()

if __name__ == "__main__":
    main()