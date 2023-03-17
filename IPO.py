from heapq import heappush, heappop

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: list[int], capital: list[int]) -> int:
        mostProfitableProjectsForCapital = {}
        placeholder = sorted(list(zip(capital, profits)))
    
        def findMostProfitableProjectsForCapital(placeholder):
            for i in range(len(placeholder)):
                if placeholder[i][0] not in mostProfitableProjectsForCapital.keys():
                    mostProfitableProjectsForCapital[placeholder[i][0]] = []
                    mostProfitableProjectsForCapital[placeholder[i][0]].append(placeholder[i][1])
                else:
                    mostProfitableProjectsForCapital[placeholder[i][0]].append(placeholder[i][1])
        findMostProfitableProjectsForCapital(placeholder)
        print(mostProfitableProjectsForCapital)
        
        h = []
        currentCapital = w
        keysToRemove=[]
        def addToHeap(capital):
            if mostProfitableProjectsForCapital == {}:
                if h == []:
                    return 0
                return -heappop(h)
            for i in mostProfitableProjectsForCapital.keys():
                if i <= capital:
                    keysToRemove.append(i)
                    for _ in range(len(mostProfitableProjectsForCapital[i])):
                        heappush(h, -mostProfitableProjectsForCapital[i][_])
                else:
                    break
            for j in keysToRemove:
                del(mostProfitableProjectsForCapital[j])
            keysToRemove.clear()
            if h == []:
                return 0
            return -heappop(h)
        for _ in range(k):
            currentCapital +=+addToHeap(currentCapital)
        return currentCapital

x = Solution()
print(x.findMaximizedCapital(k = 3, w = 0, profits = [1,2,3,1,2,3,4,5,6,7,8,9], capital = [0,0,0,1,2,3,1,2,3,1,2,3]))
# print(x.findMaximizedCapital(k = 2, w = 0, profits = [1,2,3], capital = [0,1,1]))