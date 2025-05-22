package main

import "sync"

type FizzBuzz struct {
	n            int
	fizzChan     chan any
	buzzChan     chan any
	fizzBuzzChan chan any
	numberChan   chan any
}

func Constructor(n int) *FizzBuzz {
	return &FizzBuzz{
		n:            n,
		fizzChan:     make(chan any),
		buzzChan:     make(chan any),
		fizzBuzzChan: make(chan any),
		numberChan:   make(chan any, 1),
	}
}

func (f *FizzBuzz) Fizz(printFizz func()) {
	for i, t := 0, f.n/3-f.n/15; i < t; i++ {
		f.fizzChan <- nil
		printFizz()
		<-f.numberChan
	}
}

func (f *FizzBuzz) Buzz(printBuzz func()) {
	for i, t := 0, f.n/5-f.n/15; i < t; i++ {
		f.buzzChan <- nil
		printBuzz()
		<-f.numberChan
	}
}

func (f *FizzBuzz) FizzBuzz(printFizzBuzz func()) {
	for i, t := 0, f.n/15; i < t; i++ {
		f.fizzBuzzChan <- nil
		printFizzBuzz()
		<-f.numberChan
	}
}

func (f *FizzBuzz) Number(printNumber func(i int)) {
	for i := 1; i <= f.n; i++ {
		f.numberChan <- nil
		if i%3 == 0 && i%5 == 0 {
			<-f.fizzBuzzChan
		} else if i%3 == 0 {
			<-f.fizzChan
		} else if i%5 == 0 {
			<-f.buzzChan
		} else {
			printNumber(i)
			<-f.numberChan
		}
	}
}

func main() {
	fizzBuzz := Constructor(15)
	wg := &sync.WaitGroup{}
	wg.Add(4)
	go func() {
		defer wg.Done()
		fizzBuzz.Fizz(func() {
			println("fizz")
		})
	}()
	go func() {
		defer wg.Done()
		fizzBuzz.Buzz(func() {
			println("buzz")
		})
	}()
	go func() {
		defer wg.Done()
		fizzBuzz.FizzBuzz(func() {
			println("fizzbuzz")
		})
	}()
	go func() {
		defer wg.Done()
		fizzBuzz.Number(func(i int) {
			println(i)
		})
	}()
	wg.Wait()
}
