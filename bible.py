
##
# This is Bible verse class, which will hold info about verses.
# #
# @param number Verse number.
# @param text Verse text.
#
class BibleVerse:
        #Constructor
        def __init__(self, number, text):
            self.__number = number
            self.__text = text

        def __str__(self):
            return str(self.__text)
        
        def getText(self):
              return self.__text
        
        def getNumber(self):
              return self.__number

##
# This is Bible Chapter class, which will hold info about chapter.
# #
# @param number Chapter number.
#
class BibleChapter:
        # Constructor
        def __init__(self, number):
            self.__number = number
            self.__verses = []

        def addVerse(self, verse):
              self.__verses.append(verse)

        def getVerses(self):
              return self.__verses
        
        def getNumber(self):
              return self.__number

##
# This is Bible Book class, which will hold info about bible.
# this is top level bible class.
# example: Judson Bible (Burmese)
# #
# @param name Book name.
# @param language Language that bible is written in.
#
class BibleBook:
        def __init__(self, name, language):
            self.__name = name
            self.__language = language
            self.__chapters = []
        
        def addChapter(self, chapter):
              self.__chapters.append(chapter)

        def getChapters(self):
              return self.__chapters
        
        def getName(self):
              return self.__name
        
##
# This is Bible class, which will hold info about bible.
# this is top level bible class.
#
class Bible:
        def __init__(self, name, language):
            self.__bibles = []
            self.__name = name
            self.__language = language

        def addBook(self, bible):
            self.__bibles.append(bible)

        def getBooks(self):
            return self.__bibles
        
        def getName(self):
              return self.__name



    
        


        

    
