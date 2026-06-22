class Solution:  
    def check(self, root, subroot):
       
        if not root and not subroot:
            return True
        if not root or not subroot:
            return False
       
        if root.val != subroot.val:
            return False
    
        return self.check(root.left, subroot.left) and self.check(root.right, subroot.right)
                 
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        
      
        if self.check(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)