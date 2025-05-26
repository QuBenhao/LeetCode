package main

type solution interface {
	Solve(timeout int, producers int, consumers int)
}

func main() {
	timeout := 5 // seconds
	producers := 3
	consumers := 2

	var s solution
	//// To run the answer, uncomment the following line and comment the MySolution line
	//s = &Answer{}
	s = &MySolution{}

	s.Solve(timeout, producers, consumers)
}
