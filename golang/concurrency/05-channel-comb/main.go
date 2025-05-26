package main

type solution interface {
	Solve(channels int)
}

func main() {
	channels := 3 // Number of input channels to merge

	var s solution
	//// To run the answer, uncomment the following line and comment the MySolution line
	//s = &Answer{}
	s = &MySolution{}

	s.Solve(channels)
}
