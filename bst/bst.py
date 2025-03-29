
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def bst_insert(root, i):
    curr = root
    if not curr:
        return Node(i)
    
    while True:
        if i == curr.val:
            return root
        if i < curr.val:
            if not curr.left:
                curr.left = Node(i)
                return root
            else:
                curr = curr.left
        else:
            if not curr.right:
                curr.right = Node(i)
                return root
            else:
                curr = curr.right

def bst_search(root, val):
    curr = root
    while curr:
        if curr.val == val:
            return curr
        elif curr.val < val:
            curr = curr.right
        else:
            curr = curr.left
    return None

def bst_inorder(root):
    l = []
    def _inorder(root):
        if not root:
            return
        _inorder(root.left)
        l.append(root.val)
        _inorder(root.right)

    _inorder(root)
    return l

def bst_inorder_iter(root):
    stack = []
    curr = root
    l = []
    while True:
        if curr:
            stack.append(curr)
            curr = curr.left
        else:
            if len(stack) == 0:
                break
            curr = stack.pop()
            l.append(curr.val)
            curr = curr.right
    return l

def bst_create(l):
    root = None
    for i in l:
        root = bst_insert(root, i)
    return root

def bst_height(root):
    if not root:
        return 0
    lh = bst_height(root.left)
    rh = bst_height(root.right)
    return 1 + max(lh, rh)

def bst_successor(root, val):
    res = None
    curr = root
    while curr:
        if curr.val == val:
            curr = curr.right
        elif curr.val < val:
            curr = curr.right
        else:
            res = curr.val
            curr = curr.left
    return res

def bst_predecessor(root, val):
    res = None
    curr = root
    while curr:
        if curr.val == val:
            curr = curr.left
        elif curr.val < val:
            res = curr.val
            curr = curr.right
        else:
            curr = curr.left
    return res
