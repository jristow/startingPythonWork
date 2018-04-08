#Jordan Ristow
#Implementing a queue using a circularly linked list

class CircularQueue:
    
    class _Node:
        __slots__ = '_element', '_next'
        
        def __init__(self, element, next):
            self._element = element
            self._next = next
            
    def __init__(self):
        self._tail = None
        self._size = 0
        
    def __len__(self):
        return self._size
    
    def isEmpty(self):
        return self._size == 0
    
    def first(self):
        if self.isEmpty():
            raise ValueError('Queue is empty')
        head = self._tail._next
        return head._element
    
    def dequeue(self):
        if self.isEmpty():
            raise ValueError('Queue is empty')
        oldhead = self._tail._next
        if self._size == 1:
            self._tail = None
        else:
            self._tail._next = oldhead._next
        self._size -= 1
        return oldhead._element
    
    def enqueue(self, e):
        newest = self._Node(e, None)
        if self.isEmpty():
            newest._next = newest
        else:
            newest._next = self._tail._next
            self._tail._next = newest
        self._tail = newest
        self._size += 1
        
    def rotate(self):
        if self._size > 0:
            self._tail = self._tail._next
            
def main():
    q = CircularQueue() #initializing the Queue
    
    print('Is the queue empty? ', q.isEmpty()) #testing the isEmpty function
    n = None
    while True:
        n = input('Please enter a number to add to the queue (return to quit): ') #building up the queue from user input
        if n == '':
            break
        else:
            q.enqueue(n)
            print('The new length of the queue is: ', q.__len__())
    print('The first value of the queue is: ', q.first()) #testing the first function
    q.rotate() #rotating to make a different value the first value
    for i in range(q.__len__()):
        print('The new first value of the queue is: ', q.dequeue()) #printing the first value and removing it from the queue
        print('The length of the queue is: ', q.__len__())
        
main()    
    