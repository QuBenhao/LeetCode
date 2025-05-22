import random
import threading
from typing import Callable


class Foo:
    def __init__(self):
        self.first_lock = threading.Lock()
        self.second_lock = threading.Lock()
        self.first_lock.acquire()
        self.second_lock.acquire()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.first_lock.release()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        with self.first_lock:
            # printSecond() outputs "second". Do not change or remove this line.
            printSecond()
            self.second_lock.release()

    def third(self, printThird: 'Callable[[], None]') -> None:
        with self.second_lock:
            # printThird() outputs "third". Do not change or remove this line.
            printThird()


if __name__ == "__main__":
    foo = Foo()
    thread_a = threading.Thread(target=foo.first, args=(lambda: print("first"),))
    thread_b = threading.Thread(target=foo.second, args=(lambda: print("second"),))
    thread_c = threading.Thread(target=foo.third, args=(lambda: print("third"),))

    threads = [thread_a, thread_b, thread_c]
    random.shuffle(threads)
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
