class Node:
    def __init__(self, val, left=None, right=None):
        self.left = left
        self.right = right
        self.val = val

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
                self.right = Node(val)
        if self.val >= val:
            if self.left:
                self.left.insert(val)
            else:
                self.left = Node(val)

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

    def left_rotate(self):
        ...


root = Node(10)
root.insert(5)
root.insert(20)
root.insert(30)
root.insert(15)

print(root)
print(root.max())
print(root.min())
print(root.height())

root.left_rotate()
print(root)
