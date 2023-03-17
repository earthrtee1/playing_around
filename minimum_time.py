class Solution:
    def minimumTime(self, time: list[int], totalTrips: int) -> int:
        left = 1; right = totalTrips*time[-1]
        while left < right:
            mid = int((left+right)/2)
            if sum([int(mid/x) for x in time])>=totalTrips:
                right = int(mid)
            if sum(([int(mid/x) for x in time]))<totalTrips:
                left = int(mid +1)
        return(left)
            
x = Solution()
print(x.minimumTime(time = [1, 2, 3, 5], totalTrips = 10))