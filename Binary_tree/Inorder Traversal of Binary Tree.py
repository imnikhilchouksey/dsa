# Example 1:
# Input: root = [1,null,2,3]
# Output: [1,3,2]


# Example 2:
# Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]
# Output: [4,2,6,5,7,1,3,9,8]


# Example 3:
# Input: root = []
# Output: []


# Example 4:
# Input: root = [1]
# Output: [1]

def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def inorder(root): 
            if not root : 
                return 
            inorder(root.left)
            result.append(root.val)
            inorder(root.right)
        
        inorder(root)
        return result
      