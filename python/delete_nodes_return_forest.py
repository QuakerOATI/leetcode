# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    98.15 %ile runtime
    52.66 %ile memory
    """
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        def helper(node, to_delete):
            if node is None:
                return []
            elif node.val in to_delete:
                ret = helper(node.left, to_delete).extend(helper(node.right, to_delete))
                return ret 
            forest = [node]
            for c in ["left", "right"]:
                child = node.__getattribute__(c)
                if child is not None:
                    if child.val in to_delete:
                        forest.extend(helper(child.left, to_delete))
                        forest.extend(helper(child.right, to_delete))
                        node.__setattr__(c, None)
                    else:
                        cf = helper(child, to_delete)
                        if len(cf) > 1:
                            forest.extend(cf[1:])
            return forest

        to_delete = set(to_delete)
        return helper(root, to_delete)
