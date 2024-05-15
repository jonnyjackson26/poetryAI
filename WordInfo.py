class WordInfo():
    def __init__(self):
        self.followingWords={}
        self.numOfOccurances=1 #the num of occurances for the word whos WordInfo this is 
    def addFollowingWord(self, word):
        self.numOfOccurances+=1
        if word in self.followingWords:
            self.followingWords[word]+=1
        else:
            self.followingWords[word]=1
    def toString(self):
        s="("+str(self.numOfOccurances)+"): "
        for word in self.followingWords:
            s=s+word+" ("+str(self.followingWords[word])+"), "
        return s