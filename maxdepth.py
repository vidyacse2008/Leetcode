"""
Day 5 - LeetCode 104: Maximum Depth of Binary Tree (Easy)

Given the root of a binary tree, return its maximum depth: the number of nodes
along the longest path from the root down to the farthest leaf.

Example 1:  root = [3,9,20,null,null,15,7]  ->  3
                3
               / \\
              9   20
                 /  \\
                15   7
Example 2:  root = [1,null,2]  ->  2
Example 3:  root = []          ->  0    (an empty tree has depth 0)

Constraints:
    0 <= number of nodes <= 10^4
    -100 <= node value <= 100

The guide's pattern ("Tree DFS"): solve the problem for the left subtree and the
right subtree, then combine the two answers. Decide the base case first: what is
the depth of "no node at all"?

Watch out: Python's default recursion limit is about 1000, and this tree can be
10^4 levels deep. A very deep (skewed) tree will raise RecursionError with plain
recursion. Either raise the limit with sys.setrecursionlimit, or use an
iterative approach (BFS level by level, or DFS with an explicit stack).

Run your tests with:  pytest test_maxdepth.py
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque


class Solution:
    def maxDepth(self, root):
        # BFS, one level at a time. Iterative on purpose: a recursive version
        # overflows Python's default recursion limit on very deep trees.
        if not root:
            return 0
        depth = 0
        queue = deque([root])
        while queue:
            depth += 1
            for _ in range(len(queue)):        # process exactly one level
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return depth

    # The classic recursive version (the guide's template). Fine for shallow
    # trees; needs sys.setrecursionlimit for a 10^4-deep tree.
    def maxDepthRecursive(self, root):
        if not root:
            return 0
        return 1 + max(self.maxDepthRecursive(root.left),
                       self.maxDepthRecursive(root.right))
