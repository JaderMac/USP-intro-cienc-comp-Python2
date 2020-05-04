def x1(n):
    if n >= 0 and n <= 2:
        return n
    else:
        return x1(n-1) + x1(n-2) + x1(n-3)

print(x1(6))

def x2(n):
    if n >= 0 or n <= 2:
        return n
    else:
        return x2(n-1) + x2(n-2) + x2(n-3)

print( x2(6) )