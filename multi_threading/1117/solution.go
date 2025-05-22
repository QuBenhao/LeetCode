package main

import "sync"

type Barrier struct {
	limit int
	count int
	mu    *sync.Mutex
	cond  *sync.Cond
}

func NewBarrier(limit int) *Barrier {
	mu := &sync.Mutex{}
	cond := sync.NewCond(mu)
	return &Barrier{
		limit: limit,
		count: 0,
		mu:    mu,
		cond:  cond,
	}
}

func (b *Barrier) Wait() {
	b.mu.Lock()
	defer b.mu.Unlock()
	b.count++
	if b.count == b.limit {
		b.count = 0
		b.cond.Broadcast()
	} else {
		b.cond.Wait()
	}
}

type H2O struct {
	hydrogenChan chan any
	oxygenChan   chan any
	barrier      *Barrier
}

func NewH2O() *H2O {
	hydrogenChan := make(chan any, 2)
	oxygenChan := make(chan any, 1)
	return &H2O{
		hydrogenChan: hydrogenChan,
		oxygenChan:   oxygenChan,
		barrier:      NewBarrier(3),
	}
}

func (h *H2O) Hydrogen(releaseHydrogen func()) {
	h.hydrogenChan <- nil
	h.barrier.Wait()
	releaseHydrogen()
	<-h.hydrogenChan
}

func (h *H2O) Oxygen(releaseOxygen func()) {
	h.oxygenChan <- nil
	h.barrier.Wait()
	releaseOxygen()
	<-h.oxygenChan
}

func main() {
	n := 10
	wg := &sync.WaitGroup{}
	wg.Add(n * 3)
	h2o := NewH2O()
	for i := 0; i < n; i++ {
		go func() {
			defer wg.Done()
			h2o.Hydrogen(func() {
				println("H")
			})
		}()
		go func() {
			defer wg.Done()
			h2o.Hydrogen(func() {
				println("H")
			})
		}()
		go func() {
			defer wg.Done()
			h2o.Oxygen(func() {
				println("O")
			})
		}()
	}
	wg.Wait()
}
