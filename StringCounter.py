class CharactersCalculation:
    def __init__(self):
        self.splcharacterslist = ('~', '@', '#', '$', '%', '^', '&', '*', '(', ')','-', '_', '+', '=', '{', '}', '[', ']', '|', '\\', ':', ';', '"', '\'', '<', '>', ',', '.', '?', '/')
        self.numberslist = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')
        self.vowelsletters = ('A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'u', 'U')
        self.upperCaseLetter = 0
        self.lowerCaseLetter = 0
        self.whiteSpace = 0
        self.vowelsCount = 0
        self.constantCount = 0
        self.totalCharactersCount = 0
        self.numbersCount = 0
        self.splCharactersCount = 0
    def getString(self):
        self.yourWords = str(input("Enter Your Words: "))
        self.yourWordslen = len(self.yourWords)
    def totalStringlen(self):
        for i in self.yourWords:
            if i not in (" "):
                self.totalCharactersCount += 1
    def upperCase(self):
        for i in self.yourWords:
            if (i.upper() == i and (i not in self.splcharacterslist) and (i not in self.numberslist) ):
                self.upperCaseLetter += 1
    def lowerCase(self):
        for i in self.yourWords:
            if (i.lower() == i and (i not in self.splcharacterslist) and (i not in self.numberslist)):
                self.lowerCaseLetter += 1
    def vowelsLetters(self):
        for i in self.yourWords:
            if (i in self.vowelsletters and (i not in self.splcharacterslist) and (i not in self.numberslist)):
                self.vowelsCount += 1
    def constantLetters(self):
        for i in self.yourWords:
            if (i not in self.vowelsletters and (i not in self.splcharacterslist) and (i not in self.numberslist)) :
                self.constantCount += 1
    def numberCounting(self):
        for i in self.yourWords:
            if i in self.numberslist:
                self.numbersCount += 1
    def splCharacter(self):
        for i in self.yourWords:
            if i in self.splcharacterslist:
                self.splCharactersCount += 1
    def spaceCount(self):
        for i in self.yourWords:
            if (i == " "):
                self.whiteSpace += 1
    def excute(self):
        print("It's String Calculator")
        self.getString()
        self.totalStringlen()
        self.upperCase()
        self.lowerCase()
        self.vowelsLetters()
        self.constantLetters()
        self.numberCounting()
        self.splCharacter()
        self.spaceCount()
    def display(self):
        print("Total Characters Count (without Space): ", self.totalCharactersCount)
        print("Vowel Letters Count: ", self.vowelsCount)
        print("Constant Letters Count: ", self.constantCount)
        print("UpperCase Letters Count: ", self.upperCaseLetter)
        print("LowerCase Letters Count: ", self.lowerCaseLetter)
        print("Numbers Count: ", self.numbersCount)
        print("Spl Characters Count: ", self.splCharactersCount)
        print("Total White Space Count: ", self.whiteSpace)

Calculation = CharactersCalculation()
Calculation.excute()
Calculation.display() 
