package main

type MySolution struct{}

// Solve
/**
10. Diagnosing goroutine leaks
Scenario: Given concurrent code with a leak

func leakyFunction() {
    ch := make(chan int)
    go func() {
        time.Sleep(time.Second)
        ch <- 1
    }()
    return // Return immediately
}

Requirements:
Analyze the cause of the leak
Provide two ways to fix it
Use runtime.NumGoroutine() to verify the fixes
*/
func (s *MySolution) Solve() {

}
