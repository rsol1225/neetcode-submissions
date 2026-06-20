# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #Input: root 
        #Output: length og the longst path between an two nodes within the tree 

        if root is None:
            return 0

        maxDiameter = [0]

        def height(root):

            if root is None:
                return 0 
            
            rightHeight = height(root.right)
            leftHeight = height(root.left)
            
            maxDiameter[0] = max(maxDiameter[0], rightHeight+leftHeight)

            return 1 + max(leftHeight, rightHeight)


        height(root)

        return maxDiameter[0]