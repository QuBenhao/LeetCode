package main

type MySolution struct{}

// Solve
/**
8. Cache stampede prevention
Scenario: Implement a cache that supports high concurrency:
	- When a cache entry expires, ensure only one goroutine loads the data from the database
	- Other goroutines wait for that goroutine to finish loading
	- Simulate 100 concurrent requests arriving as the cache entry expires

Requirements:
Use sync.Once or the singleflight pattern
Add a random loading delay of 100-500ms
Print the number of actual load operations
*/
func (s *MySolution) Solve(requests int) {

}
