def fib_iter(a, b, n):
    if n == 0:
        return b
    else:
        return fib_iter((a + b), b, (n-1))
        
def fib(n):
    fib_iter(1, 0, n)
    
    
def fib_iter2(n):
    a, b = 1, 0
    for i in range(n):
        a,b = a + b, a
        
    return b