def bin(n):
    if n == 1:
        return str(n)
    else:
        return ( str(bin(n//2) + str(n%2)))

print(bin(12))
