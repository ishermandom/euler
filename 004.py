def IsPalindrome(n):
    digits = str(n)
    return digits == digits[::-1]

def main():
    palindrome = 0
    for a in xrange(100, 1000):
        for b in xrange(100, 1000):
            product = a * b
            if product > palindrome and IsPalindrome(product):
                palindrome = product
    print palindrome

if __name__ == "__main__":
    main()
