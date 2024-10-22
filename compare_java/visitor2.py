"""
Python使用generator使用访问者模式
"""


class TreeNode:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __iter__(self):
        return self.__generator()

    def __generator(self):
        if self.left is not None:
            yield from iter(self.left)
        yield from self.data
        if self.right is not None:
            yield from iter(self.right)


root = TreeNode('1')
root.left = TreeNode('2')
root.right = TreeNode('3')

for ele in root:
    print(ele)
