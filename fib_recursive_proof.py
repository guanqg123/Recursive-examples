print("Following is fib(n) = fib(n-1)+fib(n-2)")
#stacking and executing like:
#call    fib(5)
#store   fib(4)+fib(3)
#call    fib(4)
#store   fib(3)+fib(2)
#call    fib(3)
#store   fib(2)+fib(1)
#call    fib(2)
#store   fib(1)+fib(0)
#call    fib(1)       #has return value
#call    fib(0)       #has return value
#compute fib(1)+fib(0)#return the value to fib(2)
#call    fib(1)       #has return value
#compute fib(2)+fib(1)#return the value to fib(3)
#call    fib(2)
#store   fib(1)+fib(0)
#call    fib(1)       #has return value
#call    fib(0)       #has return value
#compute fib(1)+fib(0)#return the value to fib(2)
#compute fib(3)+fib(2)#return the value to fib(4)
#call    fib(3)
#store   fib(2)+fib(1)
#call    fib(2)
#store   fib(1)+fib(0)
#call    fib(1)       #has return value
#call    fib(0)       #has return value
#compute fib(1)+fib(0)#return the value to fib(2)
#call    fib(1)       #has return value
#compute fib(2)+fib(1)#return the value to fib(3)
#compute fib(4)+fib(3)#return the value to fib(5)

def fib(n):
    print("call  fib({})".format(n))
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        print("store fib({})+fib({})".format(n-1,n-2))
        res = fib(n-1) + fib(n-2)
        print("Compu fib({})+fib({}), return value to fib({})".format(n-1,n-2,n))
        return res
fib(5)

print("Fllowing is fib(n-2)+fib(n-1)")

def fib(n):
    print("call  fib({})".format(n))
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        print("store fib({})+fib({})".format(n-2,n-1))
        res = fib(n-2) + fib(n-1)
        print("Compu fib({})+fib({}), return value to fib({})".format(n-2,n-1,n))
        return res
fib(5)
