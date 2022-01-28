'''You are given the root node of a binary search tree (BST) and a value to insert into the tree. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

Notice that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.

Example 1:

Input: root = [4,2,7,1,3], val = 5
Output: [4,2,7,1,3,5]'''

class Solution:
    def insertIntoBST(self, root, val):
        if root==None:
            root=TreeNode(val)
            return root
        if root.val>val:
            if root.left:
                self.insertIntoBST(root.left, val)   
            else:
                root.left=TreeNode(val)
                
        if root.val<val:
            if root.right:
                self.insertIntoBST(root.right, val)
            else:
                root.right=TreeNode(val)
                
        return root
