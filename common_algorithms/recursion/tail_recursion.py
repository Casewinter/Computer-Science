#This is unnecessary calls from the stacknot optimized because all 
def factorial(n):
    if n == 0:
        return 1
    return n  * factorial(n -1)

print(factorial(3))

#when a stack frame is called, it will be overwritten 
def o_factorial(n):
    def aux(n , acc):
        if n == 0:
            return acc
        return aux(n-1, acc*n)
    return aux(n, 1)

print(o_factorial(3))
