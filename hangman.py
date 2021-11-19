# Αυτό το παιχνίδι είναι γνωστό και ώς κρεμάλα και οι λεξεις ειναι γραμμένες στα αγγλικά
# Here we choose random name for our board
def randomFun():
    randomSelection = random.randint(0, 10)
    randomWord = things[randomSelection]
    return randomWord

# Here we keep the letter index
def letterStorage():

    pass


# Here we cut the letter from the string
def trimWord(userInput):
    count=0
    newWord=userWord
    for letter in randomWord:
        if userInput ==letter :
            newWord= newWord[:count]+ userInput+ newWord[count+1:]
    trimmed=randomWord.replace(userInput,'')
    print (newWord)
    return  trimmed, newWord


things = ['door', 'look', 'aggresive', 'book', 'positive', 'negative', 'optimistic', 'thankfull', 'poor', 'rich',
          'sensitive']
import random
print('Hello le\'s play hangman toghether')
randomWord = randomFun()
userWord = ""
trimmed = randomWord
userChoice = 6
print(' Από τη στιγμή που θα ξεκινησεις να επιλέγεις έχεις άλλες 5 προσπάθειες   ', randomWord, 'is the word')
while userWord != trimmed  and userChoice > 0:
    userInput = input('Type a letter that do you think is in the word: ').lower()
    if randomWord.find(userInput) != -1:
        userWord=trimWord(userInput)
        print(userWord)
    else:
        print('ton hpiame')

print(randomWord)
