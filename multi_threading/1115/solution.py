from typing import Callable
import threading

class FooBar:
    def __init__(self, n):
        self.n = n
        self.foo_lock = threading.Lock()
        self.bar_lock = threading.Lock()
        self.bar_lock.acquire()

    def foo(self, printFoo: 'Callable[[], None]') -> None:

        for i in range(self.n):
            # printFoo() outputs "foo". Do not change or remove this line.
            self.foo_lock.acquire()
            printFoo()
            self.bar_lock.release()

    def bar(self, printBar: 'Callable[[], None]') -> None:

        for i in range(self.n):
            # printBar() outputs "bar". Do not change or remove this line.
            self.bar_lock.acquire()
            printBar()
            self.foo_lock.release()


if __name__ == '__main__':
    n = 5
    foo_bar = FooBar(n)
    thread_a = threading.Thread(target=foo_bar.foo, args=(lambda: print("foo"),))
    thread_b = threading.Thread(target=foo_bar.bar, args=(lambda: print("bar"),))
    thread_a.start()
    thread_b.start()
    thread_a.join()
    thread_b.join()