package main

import "fmt"

const Max = 1000

func IsMultipleOf3Or5(number int) bool {
	return number % 3 == 0 || number % 5 == 0
}

func main() {
	sum := 0
	for i := 1; i < Max; i++ {
		if IsMultipleOf3Or5(i) {
			sum += i;
		}
	}

	fmt.Printf("%d\n", sum)
}
