def gcd(a, b):
    assert int(a) == a and int(b) == b, 'Enter positive Integers'
    if b == 0:
        return a
    else:
        return gcd(b, a%b)
print(gcd(99, 36))