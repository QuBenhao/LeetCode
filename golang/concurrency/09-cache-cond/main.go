package main

type solution interface {
	Solve(cacheSize int)
}

func main() {
	cacheSize := 10 // capacity of the circular buffer

	var s solution
	//// To run the answer, uncomment the following line and comment the MySolution line
	//s = &Answer{}
	s = &MySolution{}

	s.Solve(cacheSize)
}
