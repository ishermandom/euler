N = 600851475143

def NextPrime(primes):
    """Given a list of the first k primes, returns the k+1st prime."""
    # Base case: The smallest prime is 2.
    if not len(primes):
        return 2

    candidate = primes[-1]
    while True:
        candidate += 1
        for prime in primes:
            if candidate % prime == 0:
                break
        else:
            return candidate

def main():
    dividend = N
    primes = []
    prime = NextPrime(primes)
    while dividend > 1:
        if dividend % prime == 0:
            dividend /= prime
        else:
            primes.append(prime)
            prime = NextPrime(primes)

    print prime

if __name__ == "__main__":
    main()
