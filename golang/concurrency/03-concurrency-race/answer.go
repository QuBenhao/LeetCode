package main

import (
	"fmt"
	"sync"
	"sync/atomic"
	"time"
)

type Answer struct{}

type MuCounter struct {
	count int
	mu    sync.Mutex
}

type AtomicCounter struct {
	count atomic.Int32
}

type RWCounter struct {
	count int
	mu    sync.RWMutex
}

func (Answer) Solve(numProcessors int) {
	var wg sync.WaitGroup
	startTime := time.Now()
	counter := MuCounter{}
	for i := 0; i < numProcessors; i++ {
		wg.Add(1)
		go func() {
			defer wg.Done()
			counter.mu.Lock()
			defer counter.mu.Unlock()
			counter.count++
		}()
	}
	wg.Wait()
	elapsedTime := time.Since(startTime)
	fmt.Printf("Mutex final count: %d, Time taken: %s\n", counter.count, elapsedTime) // 1.2ms

	startTime = time.Now()
	atomicCounter := AtomicCounter{}
	for i := 0; i < numProcessors; i++ {
		wg.Add(1)
		go func() {
			defer wg.Done()
			atomicCounter.count.Add(1)
		}()
	}
	wg.Wait()
	elapsedTime = time.Since(startTime)
	fmt.Printf("Atomic final count: %d, Time taken: %s\n", atomicCounter.count.Load(), elapsedTime) // 0.4ms

	startTime = time.Now()
	rwCounter := RWCounter{}
	for i := 0; i < numProcessors; i++ {
		wg.Add(3)
		go func() {
			defer wg.Done()
			rwCounter.mu.Lock()
			defer rwCounter.mu.Unlock()
			rwCounter.count++
		}()
		for j := 0; j < 2; j++ {
			go func() {
				defer wg.Done()
				rwCounter.mu.RLock()
				defer rwCounter.mu.RUnlock()
				_ = rwCounter.count // Read operation
			}()
		}
	}
	wg.Wait()
	elapsedTime = time.Since(startTime)
	fmt.Printf("RWMutex final count: %d, Time taken: %s\n", rwCounter.count, elapsedTime) // 1.5ms
}
