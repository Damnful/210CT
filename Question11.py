class Node(object):
    def __init__(self, value):
          self.value = value
          self.next = None
          self.prev = None
 
class List(object):
    def __init__(self):
        self.head = None
        self.tail = None
 
    def insert(self,n,x):
        if n!=None:
            x.next = n.next
            n.next = x
            x.prev = n
            if x.next != None:
                x.next.prev = x              
        if self.head == None:
            self.head = self.tail = x
            x.prev = x.next = None
        elif self.tail == n:
            self.tail = x
 
    def delete(self, n):
        current = self.head
        #set current to be the start of the linked list
        
        while current.value != n.value:
            # loops through the list until we find node we want to delete
            if current != None:
                current = current.next
                print(current.value)
        if current.prev != None:
            # if there is a previous value, that previous value is
            # linked to the node we are deleting's next value
            current.prev.next = current.next
        if current.next != None:
            # if there is a next value, that next value is
            # linked to the node we are deleting's previous value
            current.next.prev = current.prev
 
    def display(self):
        values = []
        n = self.head
 
        while n != None:
            values.append(str(n.value))
            n = n.next
        print("List: ",",".join(values))
 
if __name__ == '__main__':
    l=List()
    l.insert(None, Node(4))
    l.insert(l.head,Node(6))
    l.insert(l.head,Node(8))
    l.insert(l.head,Node(10))
    l.insert(l.head,Node(3))
    l.insert(l.head,Node(7))
    l.insert(l.head,Node(5))
    l.display()
    l.delete(Node(10))
    l.display()
