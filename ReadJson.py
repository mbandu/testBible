import json
from abc import ABC
from IReadFile import IReadFile
from bible import Bible, BibleBook, BibleChapter, BibleVerse


class ReadJson(IReadFile):
    def __init__(self, filename):
        self.__filename = filename

    def read(self, bible):
        try:
            with open(self.__filename, 'r', encoding="utf-8-sig") as file:
                data = json.load(file)

                for book in data:
                    print(book["abbrev"])
                    print(book['name'])
                    biblebook = BibleBook( book['name'], book['abbrev'])
                    chNumber = 1
                    for chapter in book["chapters"]:
                        biblechapter = BibleChapter(chNumber)
                        biblebook.addChapter(biblechapter)
                        #print (chapter["name"])
                        for v, verseText in enumerate(chapter):
                            bibleverse = BibleVerse(v, verseText)
                            biblechapter.addVerse(bibleverse)
                            print (str(v+1) + " "  + verseText)
                    bible.addBook(biblebook)

        except FileNotFoundError:
            print("Error: File not found.")
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")