# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #remember where each value is in order
        pos={value:i for i,value in enumerate(inorder)}

        pre_index=0

        def build(left,right):
            nonlocal pre_index

            if left > right:
                return None
            
            root=TreeNode(preorder[pre_index])
            pre_index+=1

            mid=pos[root.val]

            root.left=build(left,mid-1)

            root.right=build(mid+1,right)

            return root

        return build(0,len(inorder) - 1)

        