class Node:
    def __init__(self,previous = None , data = None ,next = None ):
        self.previous = previous
        self.data = data
        self.next = next

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insertatbeginning(self,data):
        new_node = Node( data = data ,next = self.head)
        self.head = new_node
    def insertatmiddle(self,data,position):
        if self.head is None:
            self.insertatbeginning(data)
        else:
            previous_node = self.head
            for i in range(1,position-1):
                previous_node = previous_node.next
            print(previous_node.data)
            next_node = previous_node.next
            new_node = Node(previous_node , data , next_node)
            previous_node.next = next_node.previous = new_node
        
    def insertatend(self,data):
        if self.head is None :
            self.insertatbeginning(data)
        else:
            current = self.head
            while current.next != None :
                current = current.next
            new_node = Node(current , data)
            current.next = new_node
    def printt(self):
        if self.head is None:
            print("Empty List")
            return
        else:
            current = self.head
            while current:
                print(current.data,end='-->')
                current = current.next
if __name__ == "__main__":
    inst = DoublyLinkedList()
    inst.insertatbeginning(1)
    inst.insertatend(3)
    inst.insertatmiddle(2,2)
    inst.printt()
                
