N = 100

def SumUpToN(n):
    return n * (n + 1) / 2

def SumSquaresUpToN(n):
    return n * (n + 1) * (2 * n + 1) / 6

def main():
    print SumUpToN(N)**2 - SumSquaresUpToN(N)

if __name__ == "__main__":
    main()
