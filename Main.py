class node:
    def _init_(self,data):
        self.data = data
        self.prev = None
        self.next = None

class dlinkedlist:
    def _init_(self):
        self.head = None

    def is_empty(self):
        return self.head == None
    
    def emptyprint(self):
        print("The doubly linked list is empty")

    def printllfoward(self):
        if self.is_empty():
            self.emptyprint()
        else:
            n=self.head 
            while n !=None:
                print(n.data,end="-->")
                n = n.next

    def printllback(self):
        if self.is_empty():
            self.emptyprint()
        n = self.head
        while n.next is not None:
            n = n.next
        while n is not None:
            print(n.data,end="--> ")
            n = n.prev
    def insert_empty(self,data):
        if self.is_empty():
            new_node = node(data)
            self.head = new_node
        else:
            return

    def add_beg(self,data):
        if self.is_empty():
            self.insert_empty(data)
        else:
            new_node = node(data)
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def add_end(self,data):
        
        if self.is_empty():
            self.insert_empty(data)
        else:
            new_node = node(data)
            n = self.head
            while n.next is not None:
                n = n.next
            n.next = new_node
            new_node.prev = n

    def add_inbetweenafter(self,data,x):
        if self.is_empty():
            self.insert_empty(data)
        else:
            n = self.head
            while n is not None:
                if x == n.data:
                    break
                else:
                    n = n.next
            if n is None:
                print("Node is not present")
            else:
                new_node = node(data)
                new_node.next = n.next
                new_node.prev = n
                if n.next is not None:
                    n.next.prev = new_node
                n.next = new_node
                
    def add_inbetweenbefore(self,data,x):
        if self.is_empty():
            self.insert_empty(data)
        else:
            n = self.head
            while n is not None:
                if x == n.data:
                    break
                else:
                    n = n.next
            if n is None:
                print("Node is not present")
            else:
                new_node = node(data)
                new_node.next = n
                new_node.prev = n.prev
                if n.prev is not None:
                    n.prev.next = new_node
                n.prev = new_node
    def del_beg(self):
        if self.is_empty():
            self.emptyprint()
        else:
            self.head = self.head.next
            self.head.prev = None
    def del_end(self):
        if self.is_empty():
            self.emptyprint()
        else:
            n = self.head
            while n.next is not None:
                n = n.next
            n.prev.next = None
    def del_inbetween(self,x):
        if self.is_empty():
            self.emptyprint()
        else:
            n = self.head
            while n is not None:
                if x == n.data:
                    break
                else:
                    n = n.next
            if n is None:
                print("Node is not present")
            else:
                n.prev.next = n.next
                n.next.prev = n.prev
ll = dlinkedlist()
ll.add_beg(12)
ll.add_beg(13)
ll.add_inbetweenafter(20,13)
ll.add_end(19)
ll.printllback()
print("\n")
ll.del_inbetween(20)
ll.printllfoward()
