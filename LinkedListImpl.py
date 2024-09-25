#Simple Linked List Implemetation of one Node

class Node:
    def __init__(self, value):
        self.value = value
        self.next=None


class LinkedList:
    def __init__(self, value):
        newNode = Node(value)
        self.head = newNode
        self.tail=newNode
        # haed---pointer---> Node<---pointer---tail
        self.length = 1
        #indicator of length if there is any addition or deletion of a Node

newLinkedList = LinkedList(26)
print(newLinkedList.head.value)
