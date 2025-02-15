def cube(n):
    return n*n*n

def div(n):
    if n%3==0:
        return cube(n)
    else:
        return False
print (div (384))