package main

type solution interface {
	Solve(numProcessors int)
}

func main() {
	numProcessors := 1000 // Number of goroutines to increment the counter

	var s solution
	//// To run the answer, uncomment the following line and comment the MySolution line
	//s = &Answer{}
	s = &MySolution{}

	s.Solve(numProcessors)
}
