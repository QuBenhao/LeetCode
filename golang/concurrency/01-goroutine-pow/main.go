package main

type solution interface {
	Solve(numbers []int)
}

func main() {
	numbers := []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

	var s solution
	//// To run the answer, uncomment the following line and comment the MySolution line
	//s = &Answer{}
	s = &MySolution{}

	s.Solve(numbers)
}
