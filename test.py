class Node:
    def __init__(self, data: int) -> None:
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
    
    def InsertAtBegining(self, data: int) -> None:
        NewNode = Node(data)
        if self.head is None:
            self.head = NewNode
            return
        else:
            NewNode.next = self.head
            self.head = NewNode

    def printLL(self) -> None:
        if self.head is None:
            print('Linked List is Empty!')
            return
        else:
            Current_Node = self.head
            while Current_Node:
                print(Current_Node.data)
                Current_Node = Current_Node.next

    def InsertAtIndex(self, data: int, index: int) -> None:
        newNode = Node(data)
        current_node = self.head
        current_index = 0
        while current_node and current_index != index:
            temp = current_node
            current_node = current_node.next
            current_index += 1
        temp.next = newNode
        newNode.next = current_node

if __name__ == '__main__':
    linkedlist = LinkedList()
    linkedlist.InsertAtBegining(9)
    linkedlist.InsertAtBegining(10)
    linkedlist.InsertAtBegining(11)
    linkedlist.InsertAtIndex(12, 1)
    linkedlist.InsertAtIndex(13, 1)
    linkedlist.printLL()