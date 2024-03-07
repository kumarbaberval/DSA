class TreeNode:
    def __init__(self,data) -> None:
        self.data=data
        self.left=None
        self.right=None


class BinaryTree:
    def __init__(self) -> None:
        self.root=None
class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self) -> None:
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = TreeNode(data)
        else:
            self.insertrecursively(self.root, TreeNode(data))

    def insertrecursively(self, node, new_node):
        if new_node.data < node.data:
            if not node.left:
                node.left = new_node
            else:
                self.insertrecursively(node.left, new_node)
        else:
            if not node.right:
                node.right = new_node
            else:
                self.insertrecursively(node.right, new_node)

    def inorder(self, node):
        root=self.root
        if root is None:
            print('Binary Tree is Empty.')
        if node is not None:
            self.inorder(node.left)
            print(node.data)
            self.inorder(node.right)

    def preorder(self, node):
        root=self.root  
        if root is None:
            print('Binary Tree is Empty!')
        if node is not None:
            print(node.data)
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node):
        root=self.root
        if root is None:
            print('Binary Tree is Empty!')
        if node is not None:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data)

    def minimum(self):
        node=self.root
        if node is None:
            print('Tree is Empty.')
        else:
            while node.left is not None:
                node=node.left
            print(node.data)

    def minimun1(self):
        node=self.root
        while node!=None:
            left=node
            node=node.left
        print(left.data)

    def maximum(self):
        root=self.root
        if root is None:
            print('Tree is Empty.')
        else:
            while root.right is not None:
                root=root.right
            print(root.data)

    def maximum1(self):
        root=self.root
        while root!=None:
            node=root
            root=root.right
        print(node.data)

bt = BinaryTree()
bt.insert(4)
bt.insert(9)
bt.insert(2)
bt.insert(7)
bt.insert(1)
bt.insert(3)

# bt.inorder(bt.root)
# bt.preorder(bt.root)
bt.postorder(bt.root)
# print()
# print('Minimun Element: ',end=' ')
# bt.minimum()
# print('Maximum Element: ',end=' ')
# bt.maximum()
# print('Minimun Element: ',end=' ')
# bt.minimun1()
# print('Maximum Element: ',end=' ')
# bt.maximum1()