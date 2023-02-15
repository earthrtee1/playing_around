class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        def calcMedian(x:list[int]) -> float:
            match (len(x)/2).is_integer():
                case True:  
                    return (x[int(len(x)/2)] + x[int(len(x)/2)-1])/2
                case False:
                    return x[int((len(x)-1)/2)]
        if(nums1)==[]:
            return(calcMedian(nums2))
        elif(nums2)==[]:
            return(calcMedian(nums1))
        print((calcMedian(nums1) + calcMedian(nums2))/2)
        return((calcMedian(nums1) + calcMedian(nums2))/2)

x = Solution()
x.findMedianSortedArrays([1,3],[2,7])
