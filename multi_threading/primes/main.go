package main

import (
	"fmt"
	"sync"
)

func prime(base int, rd <-chan int) {
	println("prime ", base)
	hasNext := false
	curChan := make(chan int)
	var wg sync.WaitGroup
	for {
		select {
		case r, ok := <-rd:
			if !ok {
				close(curChan)
				wg.Wait()
				return
			}
			if r%base != 0 {
				if !hasNext {
					wg.Add(1)
					go func() {
						defer wg.Done()
						prime(r, curChan)
					}()
					hasNext = true
				} else {
					curChan <- r
				}
			}
		}
	}
}

func main() {
	var wg sync.WaitGroup
	var n int
	fmt.Print("Enter n: ")
	fmt.Scan(&n)
	if n < 2 {
		fmt.Println("No primes")
		return
	}
	rd := make(chan int)
	wg.Add(1)
	go func() {
		defer wg.Done()
		prime(2, rd)
	}()
	for i := 3; i <= n; i += 1 {
		rd <- i
	}
	close(rd)
	wg.Wait()
}
