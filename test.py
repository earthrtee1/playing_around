import copy

'''Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
Explanation: There are 2 shortest transformation sequences:
"hit" -> "hot" -> "dot" -> "dog" -> "cog"
"hit" -> "hot" -> "lot" -> "log" -> "cog"'''

# class Solution(object):
#     def findLadders(self, beginWord, endWord, wordList):
#         """
#         :type beginWord: str
#         :type endWord: str
#         :type wordList: List[str]
#         :rtype: List[List[str]]
#         """ 

beginWord = "hit"; endWord = "cog"; wordList = ["hot","dot","dog","lot","log","cog"]

# beginWord = "a"; endWord = "c"; wordList = ["a","b","c"]

wordDict = {}

for _ in wordList:
    wordDict[_] = 0

print(wordDict) 

def listIter(list):
    for _ in list:
        return _

counter = 1

queue =[] 

def addToQueue(word, dict, finaWord):
    lettersList = list(word)
    disposabList = copy.deepcopy(lettersList)
    print(disposabList)
    for _ in range(len(disposabList)):
        for i in range(97, 123):
            disposabList[_] = chr(i)
            print(''.join(disposabList))
            if ''.join(disposabList) in wordDict.keys():
                if wordDict[''.join(disposabList)] == 0:
                    queue.append(''.join(disposabList))
                    wordDict[''.join(disposabList)] = counter
        disposabList = copy.deepcopy(lettersList)

try:
    addToQueue(beginWord, wordDict, endWord)
    counter=counter+1
    for i in range(1000):
        addToQueue(queue[i], dict, endWord)
        counter+=1
except IndexError:
    print(1)

print(queue, "\n", wordDict)