class Solution:
    def isAlienSorted(self, words: list[str], order: str) -> bool:
        orderDict = {}
        isTrue = set()
        for i in range(len(order)):
            orderDict[order[i]]=i
        print(orderDict)     

        def checkSum(word1, word2, letterPos):
            newPos = letterPos+1
            try:
                if  orderDict[word1[letterPos]] < orderDict[word2[letterPos]]:
                    return True
                elif orderDict[word1[letterPos]] > orderDict[word2[letterPos]]:
                    isTrue.add("False")
                    return False
                else:
                    checkSum(word1, word2, newPos)
            except IndexError:
                if letterPos>=len(word1):
                    return True
                elif letterPos>=len(word2):
                    isTrue.add("False")
                    return False

        for _ in range(len(words)-1):
            checkSum(words[_],words[_+1],0)    
            if "False" in isTrue:
                print("False")
                return False
        print("True")
        return True

x = Solution()
x.isAlienSorted(["apple","app"], "abcdefghijklmnopqrstuvwxyz")