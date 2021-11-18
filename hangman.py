# Αυτό το παιχνίδι είναι γνωστό και ώς κρεμάλα και οι λεξεις ειναι γραμμένες στα αγγλικά
things = ['door', 'look', 'aggresive', 'book', 'positive', 'negative', 'optimistic', 'thankfull', 'poor', 'rich',
          'sensitive']
import random


# Here we choose random name for our board
def randomFun():
    randomSelection = random.randint(0, 10)
    randomWord = things[randomSelection]
    return randomWord

#Here we keep the letter index
def letterStorage():

    pass


# Here we cut the letter from the string
def trimWord(s):
    trimmed = randomWord
    correctLetters=[]
    count=0
    for trimLetter in randomWord:
        if trimLetter == userInput:
            trimmed = trimmed[: trimmed.find(userInput)] +" "+ trimmed[trimmed.find(userInput) + 1:]
            correctLetters.insert(count,userInput)
        count+=1
    print (correctLetters)
    return correctLetters



print('Hello le\'s play hangman toghether')
randomWord = randomFun()
userWord = ""
userChoice = 6
print(' Από τη στιγμή που θα ξεκινησεις να επιλέγεις έχεις άλλες 5 προσπάθειες   ', randomWord, 'is the word')
while randomWord != userWord and userChoice > 0:
    userInput = input('Type a letter that do you think is inn the word: ').lower()
    if randomWord.find(userInput) != -1:
        s=trimWord(userInput)
        print(s)
        print(randomWord.find(userInput))
    else:
        print('ton hpiame')

print(randomWord)
