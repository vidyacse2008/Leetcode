from maxdepth import Solution, TreeNode


def build_tree(values):
    """Build a tree from a LeetCode-style level-order list, e.g. [3,9,20,None,None,15,7]."""
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while queue and i < len(values):
        node = queue.pop(0)
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


def check(values):
    return Solution().maxDepth(build_tree(values))


def test_basic():
    assert check([3, 9, 20, None, None, 15, 7]) == 3


def test_right_only_child():
    assert check([1, None, 2]) == 2


def test_empty_tree():
    assert check([]) == 0


def test_single_node():
    assert check([0]) == 1


def test_two_levels_full():
    assert check([1, 2, 3]) == 2


def test_left_heavy_tree():
    assert check([1, 2, None, 3, None, 4]) == 4


def test_deeper_side_is_on_the_right():
    assert check([1, 2, 3, None, None, None, 4, None, 5]) == 4


def test_negative_values():
    assert check([-1, -2, -3]) == 2


def test_very_deep_skewed_tree():
    # 5000 levels, all left children: plain recursion overflows Python's default limit
    root = TreeNode(0)
    node = root
    for i in range(1, 5000):
        node.left = TreeNode(i)
        node = node.left
    assert Solution().maxDepth(root) == 5000
