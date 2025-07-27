import json
import os

VERSION = "v 1.0.0"

def main():
    
    print(f"Mini English To Spanish App {VERSION}")
    
    word = get_word()
    lang_path = "/storage/emulated/0/Documents/lang/spanish"
    def_article = "/definite_article.json"
    path = lang_path + def_article
    
    
    
    with open(path, "r") as f:
        def_article = json.load(f)
        
    if word in def_article:
        for x in range(len(def_article[word])):
            data = def_article[word][x]
            print("Translation: ", data)
    else:
        print("Word not found.")
    
  
def get_word():
    word = input("Enter the word to translate: ").lower()
    return word 
        
        
if __name__ == "__main__":
    main()