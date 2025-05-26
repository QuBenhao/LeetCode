package main

import "sync"

type FooBar struct {
	n  int
	fl sync.Mutex
	bl sync.Mutex
}

func NewFooBar(n int) *FooBar {
	obj := &FooBar{n: n}
	obj.bl.Lock()
	return obj
}

func (fb *FooBar) Foo(printFoo func()) {
	for i := 0; i < fb.n; i++ {
		fb.fl.Lock()
		// printFoo() outputs "foo". Do not change or remove this line.
		printFoo()
		fb.bl.Unlock()
	}
}

func (fb *FooBar) Bar(printBar func()) {
	for i := 0; i < fb.n; i++ {
		fb.bl.Lock()
		// printBar() outputs "bar". Do not change or remove this line.
		printBar()
		fb.fl.Unlock()
	}
}

func main() {
	fooBar := NewFooBar(5)
	foo := func() {
		println("foo")
	}
	bar := func() {
		println("bar")
	}
	wg := sync.WaitGroup{}
	wg.Add(2)
	go func() {
		defer wg.Done()
		fooBar.Foo(foo)
	}()
	go func() {
		defer wg.Done()
		fooBar.Bar(bar)
	}()
	wg.Wait()
}
