class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class List:
    def __init__(self, *args):
        self.head = Node(None, None)

        # Initialize the list
        for each in args:
            self.insert(each)

    def search(self, data):
        curr = self.head

        # Keep iterating as long as next node is not empty
        while curr.next:
            if curr.data == data:
                return curr

            curr = curr.next

        raise ValueError("Value not found in list!")

    def insert(self, data):
        new_node = Node(data=data, next=self.head)
        self.head = new_node

    def __find_predecessor(self, node):
        curr = self.head

        # Case of head deletion
        if curr.data == node.data:
            return None

        while curr.next.data != node.data:
            curr = curr.next

        return curr

    def delete(self, data):
        node = self.search(data)
        pred = self.__find_predecessor(node)

        # Head of list removed
        if not pred:
            self.head = self.head.next
        else:
            pred.next = node.next

    def __repr__(self):
        curr = self.head
        data = []

        while curr.next:
            data.append(str(curr.data))
            curr = curr.next

        return 'List({0})'.format(','.join(reversed(data)))

if __name__ == '__main__':
    l1 = List()
    l2 = List(1)
    l3 = List(1,2,3)

    l2.insert(10)
    l2.delete(1)
    l2.delete(99) # ValueError

    l3.insert(10000)

    print(l2, l3)
