package main

type solution interface {
	Solve(workers int)
}

func main() {
	workers := 4 // Number of workers

	var s solution
	//// To run the answer, uncomment the following line and comment the MySolution line
	//s = &Answer{}
	s = &MySolution{}

	s.Solve(workers)
}
