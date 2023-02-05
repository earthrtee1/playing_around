class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# try to implement for the algorythm to explore the entire side from root to leaf and backtrack all the way
class Solution:
    def sumNumbers(self, root):
        if root== None: return 0
        max_index = len(root)-1
        sum_list=[]


        def findSum(node, curr, index):
            curr = curr*10+node
            match index == 0:
                case True:
                    left = 2*index+1
                    right = 2*index+2
                case False:
                    left = 2*index+1
                    right = 2*index+2
            if left > max_index:
                sum_list.append(curr)
                return curr
            elif left == max_index:
                findSum(root[left], curr, left)
            else:
                findSum(root[left], curr, left)
                findSum(root[right], curr, right)
        findSum(root[0],0,0)
        print(sum(sum_list))
        return(sum(sum_list))
        
        


        


x = Solution()
# x.sumNumbers([4,9,0,5,1,3,5,6,7,2,5,6,3,4,6,7,9])
x.sumNumbers([1,2,3])