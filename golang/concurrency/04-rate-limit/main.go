package main

type solution interface {
	Solve(rateLimit int)
}

func main() {
	rateLimit := 5 // Number of goroutines to increment the counter

	var s solution
	//// To run the answer, uncomment the following line and comment the MySolution line
	//s = &Answer{}
	s = &MySolution{}

	s.Solve(rateLimit)
}
