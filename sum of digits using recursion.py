def SumOfDigits(n):
    if n<10:
        return n
    a = n%10
    return SumOfDigits(n//10) + a
print(SumOfDigits(232343))
