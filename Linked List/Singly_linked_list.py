class Node: # node : [data ,next]
    def __init__(self,data = None,next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self): #[Address of first node]
        self.head = None

    def insertatbeginning(self,data): 
        node = Node(data,self.head)
        self.head = node #[storing address node in head]
        print("success")

    def insertatmiddle(self,data,position):
        if self.head == None:
            self.insertatbeginning(data)
        else:
            current = self.head
            for i in range(1, position-1): # it goes to one position before the desired position
                if current is None:
                    break
                current = current.next

            if current is not None:
                new_node = Node(data, current.next)
                current.next = new_node

    def insertatend(self,data):
        if self.head == None:
            self.insertatbeginning(data)
        else:
            List = self.head
            while List.next != None:
                List.next
            new_node = Node(data)
            List.next = new_node

    def print_list(self): # Printing the data's by iterating  
        if self.head is None:
            print("Empty Linked List")
            return
        current = self.head
        while List!=None :
            print(List.data,end='-->')
            current = current.next #[storing next nodes address in current]

if __name__ == "__main__":
    inst = LinkedList()
    inst.insertatbeginning(1)
    inst.insertatend(3)
    inst.insertatmiddle(2,2)
    inst.print_list()
