package main

type solution interface {
	Solve(serverNum int, timeoutMs int)
}

func main() {
	serverNum := 3   // Number of servers to request
	timeoutMs := 500 // Timeout in milliseconds

	var s solution
	//// To run the answer, uncomment the following line and comment the MySolution line
	//s = &Answer{}
	s = &MySolution{}

	s.Solve(serverNum, timeoutMs)
}
