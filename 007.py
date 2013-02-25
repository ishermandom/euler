N = 10001

def NextPrime(primes_and_squares):
    """Given a list of the first k primes and their squares, returns the k+1st prime."""
    # Base case: The smallest prime is 2.
    if not len(primes_and_squares):
        return 2

    candidate = primes_and_squares[-1][0]
    while True:
        candidate += 1
        for (prime, square) in primes_and_squares:
            if square > candidate:
                return candidate
            if candidate % prime == 0:
                break
        else:
            return candidate

def main():
    primes_and_squares = []
    while len(primes_and_squares) < N:
        prime = NextPrime(primes_and_squares)
        primes_and_squares.append((prime, prime**2))

    print primes_and_squares[-1][0]

if __name__ == "__main__":
    main()
