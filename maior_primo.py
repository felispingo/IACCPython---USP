import sys

def ePrimo(n):
    m = 0
    i = 0
    for c in range(1, n + 1):
        if n % c == 0:
            m = m + 1
    if m == 2:
        return(n)
    else:
        i = i + 1
        ePrimo(n-i)
        eprint(n-i)



def maior_primo(n):
    if n < 2:
        sys.exit("Apenas valores positivos")
    else:
        ePrimo(n)
