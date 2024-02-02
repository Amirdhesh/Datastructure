class Node:
    def __init__(self , data = None , next = None):
        self.data = data
        self.next = next
class CircularList:
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
            temp.next = new_node
            new_node.next = self.head
            self.head = new_node
    def apprend(self,data):
        new_node = Node(data = data)
        if self.head is None:
            self.head = new_node
            new_node = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head
    def insertatmiddle(self,data,position):
        new_node = Node(data = data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head
            for i in range(1,position - 1):
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node
    def print(self):
        if self.head is None:
            print("Empty List")
        else:
            temp = self.head
            while temp.next != self.head:
                print(temp.data,end = '-->')
                temp = temp.next
            print(temp.data)

if __name__ == "__main__":
    inst = CircularList()
    inst.insertatbeginning(1)
    inst.apprend(2)
    inst.insertatmiddle(3,2)
    inst.print()
