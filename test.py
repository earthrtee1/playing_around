import copy

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):

        self.beginWord = beginWord; self.endWord = endWord; self.wordList = wordList

        #create a dict with a number of steps to reach each word as a value
        wordDict = {}

        for _ in wordList:
            wordDict[_] = 0

        # check if the endWord is in the wordDict:
        if endWord not in wordDict.keys():
            return 0

        #queue to add words that were encoutered from the wordList
        queue =[] 

        #fucntion to add words encoutered in the wordList to the queue
        # variables: word -> word from queue to iterate over, dict -> wordDict to check if the word was encountered before, finalWord -> endWord
        def addToQueue(word, dict, finalWord):
            # split the word into a list of letters
            lettersList = list(word)
            # create a deepcopy of the split word list to change without changing the primary list
            disposabList = copy.deepcopy(lettersList)
            # loop to iter over each letter in a word
            for _ in range(len(disposabList)):
                # loop to iter each lowercase letter in the alphabet
                for i in range(97, 123):
                    # replace _ letter in the word with each lowercase letter in the alphabet
                    disposabList[_] = chr(i)
                        # print(disposabList)
                    # print(''.join(disposabList))
                    # check if the resulted word is in the dictionary and if it was encountered before:
                    if ''.join(disposabList) in wordDict.keys() and wordDict[''.join(disposabList)] == 0:
                        queue.append(''.join(disposabList))
                        # print(''.join(disposabList))
                        if word == beginWord:
                            wordDict[''.join(disposabList)] = 1
                        else:
                            wordDict[''.join(disposabList)] = wordDict[word] + 1
                disposabList = copy.deepcopy(lettersList)

        try:
            addToQueue(beginWord, wordDict, endWord)
            for i in range(10000):
                addToQueue(queue[i], wordDict, endWord)
                # print(queue)
        except IndexError:
            pass
            # print(wordDict)
        if wordDict[endWord]==0:
            return 0
        else:
            return(wordDict[endWord]+1)
