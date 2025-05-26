package main

import (
	"fmt"
	"math/rand"
	"sync"
)

type Foo struct {
	muFirst  sync.Mutex
	muSecond sync.Mutex
}

func Constructor() *Foo {
	obj := &Foo{}
	obj.muFirst.Lock()
	obj.muSecond.Lock()
	return obj
}

func (f *Foo) first(printFirst func()) {
	printFirst()
	f.muFirst.Unlock()
}

func (f *Foo) second(printSecond func()) {
	f.muFirst.Lock()
	printSecond()
	f.muFirst.Unlock()
	f.muSecond.Unlock()
}

func (f *Foo) third(printThird func()) {
	f.muSecond.Lock()
	printThird()
}

func main() {
	foo := Constructor()
	threads := make([]func(), 3)
	wg := sync.WaitGroup{}
	wg.Add(3)
	threads[0] = func() { foo.first(func() { fmt.Println("first") }); wg.Done() }
	threads[1] = func() { foo.second(func() { fmt.Println("second") }); wg.Done() }
	threads[2] = func() { foo.third(func() { fmt.Println("third") }); wg.Done() }
	rand.Shuffle(len(threads), func(i, j int) { threads[i], threads[j] = threads[j], threads[i] })
	for _, thread := range threads {
		go thread()
	}
	wg.Wait()
}
