package main

import (
	"fmt"
	"sync"
)

type Answer struct{}

func (Answer) Solve(numbers []int) {
	var wg sync.WaitGroup
	for _, num := range numbers {
		wg.Add(1)
		go func(n int) {
			defer wg.Done()
			fmt.Printf("Square of %d is %d\n", n, n*n)
		}(num)
	}
	wg.Wait()
}
