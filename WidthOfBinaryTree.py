class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        level = [(root, 0)] # the tuple keeps track of the node and its index in that level of the tree
        maximum = 1
        
        while level:
            maximum = max(maximum, level[-1][1] - level[0][1] + 1)
            new_level = []
            for node, place in level:
                if node.left: new_level.append((node.left, 2*place))
                if node.right: new_level.append((node.right, 2*place + 1))
            level = new_level
            
        return maximum