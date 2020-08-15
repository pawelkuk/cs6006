class Node:
    def __init__(self, val, parent, left=None, right=None):
        self.left = left
        self.right = right
        self.val = val
        self.parent = parent

    def __str__(self):
        return (
            f"Node(val={self.val},{self.left if self.left else ''},"
            f"{self.right if self.right else ''})"
        )

    def insert(self, val):
        if self.val < val:
            if self.right:
                return self.right.insert(val)
            else:
                self.right = Node(val, self)
                return self.right
        if self.val >= val:
            if self.left:
                return self.left.insert(val)
            else:
                self.left = Node(val, self)
                return self.left

    def max(self):
        if self.right:
            return self.right.max()
        else:
            return self.val

    def min(self):
        if self.left:
            return self.left.min()
        else:
            return self.val

    def height(self):
        if self.left and self.right:
            return 1 + max(self.left.height(), self.right.height())
        if self.left and not self.right:
            return 1 + self.left.height()
        if not self.left and self.right:
            return 1 + self.right.height()
        return 0


class AVL:
    def __init__(self, val):
        self.root = Node(val, parent=None)

    def left_rotate(self, x):
        y = x.right
        y.parent = x.parent
        if y.parent is None:
            self.root = y
        else:
            if y.parent.left is x:
                y.parent.left = y
            elif y.parent.right is x:
                y.parent.right = y
        x.right = y.left
        if x.right is not None:
            x.right.parent = x
        y.left = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left
        y.parent = x.parent
        if y.parent is None:
            self.root = y
        else:
            if y.parent.left is x:
                y.parent.left = y
            elif y.parent.right is x:
                y.parent.right = y
        x.left = y.right
        if x.left is not None:
            x.left.parent = x
        y.right = x
        x.parent = y

    def rebalance(self, node):
        while node is not None:
            lh = node.left.height() if node.left else 0
            rh = node.right.height() if node.right else 0
            if lh >= 2 + rh:
                llh = node.left.left.height() if node.left.left else 0
                lrh = node.left.right.height() if node.left.right else 0
                if llh >= lrh:
                    self.right_rotate(node)
                else:
                    self.left_rotate(node.left)
                    self.right_rotate(node)
            elif rh >= 2 + lh:
                rrh = node.right.right.height() if node.right.right else 0
                rlh = node.right.left.height() if node.right.left else 0
                if rrh >= rlh:
                    self.left_rotate(node)
                else:
                    self.right_rotate(node.right)
                    self.left_rotate(node)
            node = node.parent

    def insert(self, val):
        node = self.root.insert(val)
        self.rebalance(node)


avl = AVL(10)
avl.insert(5)
avl.insert(6)
avl.insert(3)
avl.insert(8)
avl.insert(9)
avl.insert(4)
avl.insert(2)
avl.insert(1)
avl.insert(20)
avl.insert(30)
avl.insert(15)

print(avl.root)
print(avl.root.max())
print(avl.root.min())
print(avl.root.height())
print(avl.root)
