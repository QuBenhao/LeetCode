package main

import (
	"fmt"
	"sync"
	"time"
)

type Answer struct{}

func processRequest(ch chan any, id int) {
	// Simulate processing a request
	start := time.Now()
	ch <- nil
	time.Sleep(time.Second)
	end := time.Now()
	fmt.Printf("Request %d processed in %v. [start at %v][end at %v]\n", id, end.Sub(start), start, end)
	<-ch // Release the slot in the channel
}

func (Answer) Solve(rateLimit, requests int) {
	ch := make(chan any, rateLimit)
	defer close(ch)
	var wg sync.WaitGroup
	for i := range requests {
		wg.Add(1)
		go func() {
			defer wg.Done()
			processRequest(ch, i+1)
		}()
	}
	wg.Wait()
}
