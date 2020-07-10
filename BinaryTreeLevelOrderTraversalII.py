class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return
        level=0
        res=[]
        return self.levelOrder(root,level,res)
        
    def levelOrder(self,root,level,res):
        if not root:
            return
        if len(res)==level:
            res.append([])
        res[level].append(root.val)
        self.levelOrder(root.left,level+1,res)
        self.levelOrder(root.right,level+1,res)
        return res[::-1]
        