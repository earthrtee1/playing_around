#    try to implement for the algorythm to explore the entire side from root to leaf and backtrack all the way
class Solution:
    def sumNumbers(self, root: TreeNode):
        def checkNode(root, curr):
            if root == None: return 0
            curr += curr*10+root.val
            if root.left == None and root.right == None:
                return curr
            return(checkNode(root.left, curr) + checkNode(root.right, curr))
        return checkNode(root, 0)


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(root, cur):
            if not root: return 0
            cur = cur * 10 + root.val
            if not root.left and not root.right:
                return cur
            return dfs(root.left, cur) + dfs(root.right, cur)
        return dfs(root, 0)
        
        


        


x = Solution()
# x.sumNumbers([4,9,0,5,1,3,5,6,7,2,5,6,3,4,6,7,9])
x.sumNumbers([1,2,3])