class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def dfs(self, root1, root2) -> bool:
        if root1 is None and root2 is None:
            return True
        elif root1 is not None and root2 is not None:
            if root1.val != root2.val:
                return False

            return self.dfs(root1.left, root2.left) and self.dfs(root1.right, root2.right)
        else:
            return False

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        return self.dfs(p, q)


s = Solution()
