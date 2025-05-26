package main

type solution interface {
	Solve(requests int)
}

func main() {
	requests := 100 // Number of requests to process

	var s solution
	//// To run the answer, uncomment the following line and comment the MySolution line
	//s = &Answer{}
	s = &MySolution{}

	s.Solve(requests)
}
