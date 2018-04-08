# Jordan Ristow
#Implementing a deque using a linked list

class _DoublyLinkedBase:
    
    class _Node:
        __slots__ = '_element', '_prev', '_next'
        
        def __init__(self, element, prev, next):
            self._element = element
            self._prev = prev
            self._next = next
    
    def __init__(self):
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0
        
    def __len__(self):
        return self._size
    
    def isEmpty(self):
        return self._size == 0
    
    def _insert_between(self, e, predecessor, successor):
        newest = self._Node(e, predecessor, successor)
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest
    
    def _delete_node(self, node):
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        element = node._element
        node._prev = node._next = node._element = None
        return element
    
class LinkedDeque(_DoublyLinkedBase):
        
    def first(self):
        if self.isEmpty():
            raise ValueError('Deque is empty')
        return self._header._next._element
        
    def last(self):
        if self.isEmpty():
            raise ValueError('Deque is empty')
        return self._trailer._prev._element
        
    def insertFirst(self, e):
        self._insert_between(e, self._header, self._header._next)
            
    def insertLast(self, e):
        self._insert_between(e, self._trailer._prev, self._trailer)
            
    def deleteFirst(self):
        if self.isEmpty():
            raise ValueError('Deque is empty')
        return self._delete_node(self._header._next)
        
    def deleteLast(self):
        if self.isEmpty():
            raise ValueError('Deque is empty')
        return self._delete_node(self._trailer._prev)
        
def main():
    dq = LinkedDeque() #initializing the deque
    
    print('Is the deque empty? ', dq.isEmpty()) #testing isEmpty function
    
    lastValue = input('What is the last value in your deque? ')
    dq.insertLast(lastValue) #adding a value in the last position
    
    sentinel = None
    #This loop builds a deque with a succession of first value insertions
    while True:
        sentinel = input('Please enter the next value you want to add to the deque (return to quit): ')
        if sentinel == '':
            break
        else:
            dq.insertFirst(sentinel)
            print(dq.__len__())
            
    print('The first item in this deque is: ', dq.deleteFirst()) #removing the first value of the deque and printing it
    
    #This loop prints the last value from the deque as it removes them
    for i in range(dq.__len__()):
        print('Removing the last item from the deque.')
        print(dq.deleteLast())
        print(dq.__len__())
        
main()