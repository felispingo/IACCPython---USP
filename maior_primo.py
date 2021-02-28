import sys

def proxPrimo(n):
    i = 0
    i = i + 1
    ePrimo(n-i)
    P = (n - i)
    print(P)



def ePrimo(n):
    m = 0
    for c in range(1, n + 1):
        if n % c == 0:
            m = m + 1
    if m == 2:
        return(n)
    else:
        proxPrimo(n)



def maior_primo(n):
    if n < 2:
        sys.exit("Apenas valores positivos")
    else:
        ePrimo(n)
