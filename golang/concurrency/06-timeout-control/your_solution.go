package main

type MySolution struct{}

// Solve
/**
6. Timeout handling
Scenario: Implement a network request function with these requirements:
	- Query three mirror servers concurrently
	- Use the first response received
	- Cancel all requests automatically after 500ms
	- Print the ID of the server whose response is used

Requirements:
Use context.WithTimeout
Ensure unfinished goroutines do not leak
Handle possible panics
*/
func (s *MySolution) Solve(serverNum int, timeoutMs int) {

}
