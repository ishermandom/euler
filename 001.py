MAX = 1000

def IsMultipleOf3Or5(number):
    return number % 3 == 0 or number % 5 == 0

def main():
    print sum(filter(IsMultipleOf3Or5, xrange(1, MAX)))

if __name__ == "__main__":
    main()
