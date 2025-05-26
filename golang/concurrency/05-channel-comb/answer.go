package main

import (
	"fmt"
	"math/rand/v2"
)

type Answer struct{}

func fanIn(output chan<- any, inputs ...chan any) {
	runs := len(inputs)
	for runs > 0 {
		select {
		case v, ok := <-inputs[0]:
			if ok {
				output <- v
			} else {
				runs--
			}
		case v, ok := <-inputs[1]:
			if ok {
				output <- v
			} else {
				runs--
			}
		case v, ok := <-inputs[2]:
			if ok {
				output <- v
			} else {
				runs--
			}
		}
	}
	close(output)
}

func (Answer) Solve(channels int) {
	inputs := make([]chan any, channels)
	output := make(chan any)
	for i := 0; i < channels; i++ {
		inputs[i] = make(chan any)
		go func(ch chan<- any, id int) {
			for j := range rand.IntN(5) + 1 {
				ch <- id*10 + j
			}
			close(ch)
		}(inputs[i], i)
	}
	go fanIn(output, inputs...)
	for v := range output {
		fmt.Println(v)
	}
	<-output // Wait for the output channel to be closed
	fmt.Println("All channels merged successfully.")
}
