MAX = 20

def GreatestCommonDivisor(a, b):
    if b == 0:
        return a

    return GreatestCommonDivisor(b, a % b)

def LeastCommonMultiple(a, b):
    return a * b / GreatestCommonDivisor(a, b)

def main():
    multiple = 1
    for n in xrange(1, MAX + 1):
        multiple = LeastCommonMultiple(multiple, n)

    print multiple

if __name__ == "__main__":
    main()
