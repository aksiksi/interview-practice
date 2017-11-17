class Node:
    def __init__(self, data=None, parent=None, left=None, right=None):
        self.data = data
        self.parent = parent
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self, root):
        # Root node
        self.root = Node(root, None, None, None)

    def search(self, data):
        """
            Finds and returns the node containing the given data.
        """
        curr = self.root

        while curr:
            if curr.data == data:
                return curr

            if data < curr.data:
                curr = curr.left
            else:
                curr = curr.right

        raise ValueError("Value not found in tree!")

    def min(self):
        """
            Finds the minimum value in a binary search tree.
            The min is -- by definition -- the *leftmost* value in the tree.
        """
        curr = self.root

        while curr and curr.left:
            curr = curr.left

        return curr

    def traverse(self):
        """
            Traverses the tree by visiting each node in order.
            Appends values to data list and returns the list.
        """
        def __traverse(root, l):
            if root:
                __traverse(root.left, l)
                l.append(root.data)
                __traverse(root.right, l)

        data = []
        __traverse(self.root, data)

        return data

    def insert(self, data):
        curr = self.root
        parent = None

        # Find suitable position to insert new node
        while curr:
            if data < curr.data:
                parent = curr
                curr = curr.left
            else:
                parent = curr
                curr = curr.right

        if data > parent.data:
            parent.right = Node(data, parent, None, None)
        else:
            parent.left = Node(data, parent, None, None)

    def __repr__(self):
        data = self.traverse()
        return 'BinaryTree({0})'.format(','.join([str(e) for e in data]))


if __name__ == '__main__':
    b = BinaryTree(1)
    b.insert(5)
    b.insert(15)
    print(b)
