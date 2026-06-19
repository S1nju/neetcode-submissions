# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        visited = []
        if not root:
            return

        
        if root not in visited:
            temp = root.right
            root.right = root.left
            root.left = temp
            visited.append(root)
        
        self.invertTree(root.right)
        self.invertTree(root.left)
        return root
        
        
        
        
             
        