k = int(input())

def fibonacci(n):
    fib1, fib2 = 0, 1
    res=[]
    while len(res) < n:      
        fib1, fib2 = fib2, fib1 + fib2
        res.append(fib1) 
    return res
print(fibonacci(k))
