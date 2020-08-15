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
                self.right.insert(val)
            else:
                self.right = Node(val, self)
        if self.val >= val:
            if self.left:
                self.left.insert(val)
            else:
                self.left = Node(val, self)

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


avl = AVL(10)
avl.root.insert(5)
avl.root.insert(20)
avl.root.insert(30)
avl.root.insert(15)

print(avl.root)
print(avl.root.max())
print(avl.root.min())
print(avl.root.height())

avl.left_rotate(avl.root)
print(avl.root)

avl.right_rotate(avl.root)

print(avl.root)
