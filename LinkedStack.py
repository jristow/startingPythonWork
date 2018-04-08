# Jordan Ristow
# Implementing a stack using a linked list

class LinkedStack:
    
    class _Node:
        __slots__ = '_element', '_next'
        
        def __init__(self, element, next):
            self._element = element
            self._next = next
            
    def __init__(self):
        self._head = None
        self._size = 0
        
    def __len__(self):
        return self._size
    
    def isEmpty(self):
        return self._size == 0
    
    def push(self, e):
        self._head = self._Node(e, self._head)
        self._size += 1
        
    def top(self):
        if self.isEmpty():
            raise ValueError('Stack is empty')
        return self._head._element
    
    def pop(self):
        if self.isEmpty():
            raise ValueError('Stack is empty')
        value = self._head._element
        self._head = self._head._next
        self._size -= 1
        return value
    
def main():
    s = LinkedStack()  #creates the stack
    print('Is the stack empty? ', s.isEmpty())  #Testing the isEmpty function
    repetitions = int(input('How many elements do you want to add to the stack? '))
    for i in range(repetitions):  #building up the stack based on the number of elements the user selected
        n = int(input('Please enter a number to add to the stack: '))
        s.push(n)
    
    print('What value is at the top of the stack? ',s.top()) #Returns the top value of the stack without deleting it
    
    for i in range(repetitions): #decomposing the stack by popping the first value off one by one
        print('Current length of the stack: ', s.__len__())
        print('Top value: ', s.pop())
        
    print('What value is at the top of the stack?')
    s.top() #testing the empty ValueError of the top function
        
    
    
main()