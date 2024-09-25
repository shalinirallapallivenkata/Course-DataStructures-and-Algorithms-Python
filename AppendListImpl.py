class Node:
    def __init__(self, value):
        self.value=value
        self.next=None

class LinkedList:
    def __init__(self, value):
        newNode = Node(value)
        self.head= newNode
        self.tail = newNode
        self.length = 1

    def printList(self):
        temp=self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next

    def append(self, value):
        newNodeAppend= Node(value)
        if self.length==0:
            self.head = newNodeAppend
            self.tail = newNodeAppend
        else:
            self.tail.next= newNodeAppend
            self.tail = newNodeAppend
            # not necessary
            self.tail.next = None
        self.length +=1

newLiskedList = LinkedList(26)
newLiskedList.append(1990)

newLiskedList.printList()

        