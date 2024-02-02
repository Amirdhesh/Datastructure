class Node:
    def __init__(self, previous = None , data = None , next = None):
        self.previous = previous
        self.data = data
        self.next = next
class DoublyCircularList:
    def __init__(self):
        self.head = None
    def insertatbeginning(self,data):
        new_node = Node(data = data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            new_node.previous = temp
            temp.next = new_node
            new_node.next = self.head
            self.head = new_node
    def append(self , data):
        new_node = Node(data = data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            new_node.previous = temp
            temp.next = new_node
            new_node.next = self.head
    def insertatmiddle(self , data , position):
        new_node = Node(data = data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head
            for i in range(1,position-1):
                temp = temp.next
            new_node.next = temp.next
            temp.next.previous = new_node
            temp.next = new_node
            new_node.previous = temp
    def print(self):
        if self.head is None:
            print("Empty List")
            return
        else:
            temp = self.head
            while temp.next != self.head:
                print(temp.data, end = "-->")
                temp = temp.next
            print(temp.data)

if __name__ == "__main__":
    inst = DoublyCircularList()
    inst.insertatbeginning(1)
    inst.append(3)
    inst.insertatmiddle(2,2)
    inst.print()
