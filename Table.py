from WordInfo import WordInfo
import random

class Table():
    def __init__(self, words):
        self.table={}
        for i in range(len(words) - 1):
            current_word = words[i]
            next_word = words[i + 1]
            
            if current_word in self.table:
                self.table[current_word].addFollowingWord(next_word)
            else:
                self.table[current_word] = WordInfo()
                self.table[current_word].addFollowingWord(next_word)

        #write results to ouptut/output.txt
        with open("output/output.txt", "w") as output_file:
            for word in self.table:
                output_file.write(word + " " + self.table[word].toString() + "\n")

    def continueGenerating(self, moreWords=100):
        #make a list 
        generatedWords=[]
        generatedWords.append(random.choice(list(self.table.keys()))) #randomly picked starting word
        for _ in range(moreWords):
            generatedWords.append(self.getNextWord(generatedWords[-1]))
        extraWords= " ".join(generatedWords)
        #write to file
        with open("output/generatedContinuation.txt", 'w') as output_file:
            output_file.write(extraWords)
    
    def getNextWord(self, lastWord):
        #pick a random word from the words that follow 'lastWord'
        wordInfo=self.table[lastWord]
        return wordInfo.getRandomWordThatCouldFollow() 