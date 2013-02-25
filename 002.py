MAX = 4000000

def main():
    terms = [0, 1]
    while terms[-1] < MAX:
        terms.append(terms[-2] + terms[-1])

    print sum(filter(lambda x: x % 2 == 0, terms))

if __name__ == "__main__":
    main()
