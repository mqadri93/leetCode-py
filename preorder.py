"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return []
        preorder_list = []
        preorder_list.append(root.val)
        for n in root.children:
            preorder_list.extend(self.preorder(n))
        return preorder_list
