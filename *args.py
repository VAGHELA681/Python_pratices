def add(*args):
    print(args)
    
add(10 , 20 , 30 , 40)
print()


def sum(*args):
    total = 0
    
    for i in args:
        total = total + i
    
    print(total)

sum(10, 10)
