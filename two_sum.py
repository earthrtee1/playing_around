class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        numsSorted = sorted(nums)
        slices = [None, None]
        
        def findNextSlice(currentPos: int, currentSlice: list[int]) -> list[int]:
            x = currentSlice
            if x == [None, None]:
                for i in range(len(numsSorted)):
                    if (numsSorted[0] + numsSorted[-1-i]) > target:
                        continue
                    elif (numsSorted[0] + numsSorted[-1-i]) == target:
                        return(numsSorted[0], numsSorted[-1-i])
                    else:
                        slices[0] = 0; slices[1] = numsSorted[-1-i]
                        break
            else:
                for i in range(len(numsSorted[slices[0]:slices[1]+1])):
                    if (numsSorted[0] + numsSorted[-1-i]) > target:
                        continue
                    elif (numsSorted[0] + numsSorted[-1-i]) == target:
                        return(numsSorted[0], numsSorted[-1-i])
                    else:
                        slices[0] = currentPos; slices[1] = numsSorted[-1-i]
                        break
        
        for i in range(len(numsSorted)):
            x = findNextSlice(i, slices)
            if x != None:
                if nums.index(x[0]) != nums.index(x[1]):
                    return [nums.index(x[0]),nums.index(x[1])]
                else:
                    return [nums.index(x[0]),nums.index(x[1], nums.index(x[0])+1)]
x = Solution()
print(x.twoSum(nums = [3,2,3], target = 6))

        
