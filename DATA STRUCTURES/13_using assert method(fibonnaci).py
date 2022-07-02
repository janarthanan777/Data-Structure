def fibonnaci(n):
    assert n >= 0 and int(n) == n, 'Enter a positive Integer'
    if n in [1, 2, 0]:
        return 1
    else:

        return (fibonnaci(n-1) + fibonnaci(n-2))
x = int(input('Enter the number of fibonacci series you wanna look'))
for a in range(1, x):
    print(fibonnaci(a))

