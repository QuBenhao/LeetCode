package main

import "sync"

type ZeroEvenOdd struct {
	n        int
	zeroLock sync.Mutex
	evenLock sync.Mutex
	oddLock  sync.Mutex
}

func NewZeroEvenOdd(n int) *ZeroEvenOdd {
	obj := &ZeroEvenOdd{n: n}
	obj.oddLock.Lock()
	obj.evenLock.Lock()
	return obj
}

func (z *ZeroEvenOdd) Zero(printNumber func(int)) {
	for i := 0; i < z.n; i++ {
		z.zeroLock.Lock()
		printNumber(0)
		if i%2 == 0 {
			z.oddLock.Unlock()
		} else {
			z.evenLock.Unlock()
		}
	}
}

func (z *ZeroEvenOdd) Even(printNumber func(int)) {
	for i := 2; i <= z.n; i += 2 {
		z.evenLock.Lock()
		printNumber(i)
		z.zeroLock.Unlock()
	}
}

func (z *ZeroEvenOdd) Odd(printNumber func(int)) {
	for i := 1; i <= z.n; i += 2 {
		z.oddLock.Lock()
		printNumber(i)
		z.zeroLock.Unlock()
	}
}

func main() {
	zeo := NewZeroEvenOdd(5)
	printNumber := func(n int) {
		println(n)
	}
	wg := sync.WaitGroup{}
	wg.Add(3)
	go func() {
		defer wg.Done()
		zeo.Zero(printNumber)
	}()
	go func() {
		defer wg.Done()
		zeo.Even(printNumber)
	}()
	go func() {
		defer wg.Done()
		zeo.Odd(printNumber)
	}()
	wg.Wait()
}
