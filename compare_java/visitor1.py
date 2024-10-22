"""
Python实现Java访问者模式

Visitor模式的本质在于分离结构和操作
"""


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def accept(self, visitor):
        if self.left is not None:
            self.left.accept(visitor)
        visitor.visit(self)
        if self.right is not None:
            self.right.accept(visitor)


class PrintVisitor:

    def visit(self, node):
        print(node.data)


root = TreeNode('1')
root.left = TreeNode('2')
root.right = TreeNode('3')

visitor = PrintVisitor()

root.accept(visitor)