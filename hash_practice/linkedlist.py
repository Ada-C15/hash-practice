class Node:
    def __init__(self, value, next=None):
        self.data = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    #addNode() will add a new node to the list  
    def add_node(self, data):  
        #Create a new node  
        new_node = Node(data);  
          
        #Checks if the list is empty  
        if(self.head == None):  
            #If list is empty, both head and tail will point to new node  
            self.head = new_node;  
            self.tail = new_node;  
        else:  
            #newNode will be added after tail such that tail's next will point to newNode  
            self.tail.next = new_node;  
            #newNode will become new tail of the list  
            self.tail = new_node;  

    def add_first(self, value):
        new_node = Node(value)

        new_node.next = self.head
        self.head = new_node

    def to_list(self):
        current = self.head
        my_list = []
        while(current != None):  
            my_list.append(current.data)
            #Node index will point to node next to current  
            current = current.next;  
        return my_list