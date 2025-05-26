package main

import (
	"context"
	"fmt"
	"math/rand/v2"
	"sync"
	"time"
)

type Answer struct{}

func producer(ctx context.Context, id int, ch chan<- int) {
	for {
		select {
		case <-ctx.Done():
			fmt.Printf("Producer %d done\n", id)
			return
		default:
			// Simulate producing a random number
			ch <- rand.IntN(100) + 1    // Random number between 1 and 100
			time.Sleep(1 * time.Second) // Simulate time taken to produce
		}
	}
}

func consumer(ctx context.Context, id int, ch <-chan int) {
	for {
		select {
		case <-ctx.Done():
			fmt.Printf("Consumer %d done\n", id)
			return
		case num := <-ch:
			// Print the received number with consumer ID
			fmt.Printf("Consumer %d received: %d\n", id, num)
		}
	}
}

func (Answer) Solve(timeout int, producers int, consumers int) {
	ctx, cancel := context.WithTimeout(context.Background(), time.Duration(timeout)*time.Second)
	defer cancel()
	ch := make(chan int)
	defer close(ch)

	var wg sync.WaitGroup
	for i := range producers {
		wg.Add(1)
		go func() {
			defer wg.Done()
			producer(ctx, i+1, ch)
		}()
	}
	for i := range consumers {
		wg.Add(1)
		go func() {
			defer wg.Done()
			consumer(ctx, i+1, ch)
		}()
	}
	wg.Wait()
}
