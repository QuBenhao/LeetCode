from typing import Callable
import threading


class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.count = 0
        self.zero_lock = threading.Lock()
        self.odd_lock = threading.Lock()
        self.even_lock = threading.Lock()
        self.odd_lock.acquire()
        self.even_lock.acquire()

    # printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(self.n):
            self.zero_lock.acquire()
            printNumber(0)
            if i % 2 == 0:
                self.odd_lock.release()
            else:
                self.even_lock.release()

    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(2, self.n+1,2):
            self.even_lock.acquire()
            self.count += 1
            printNumber(i)
            self.zero_lock.release()

    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n+1, 2):
            self.odd_lock.acquire()
            printNumber(i)
            self.zero_lock.release()


if __name__ == "__main__":
    zeo = ZeroEvenOdd(5)

    def print_number(x: int):
        print(x)

    threads = [threading.Thread(target=zeo.zero, args=(print_number,)),
               threading.Thread(target=zeo.even, args=(print_number,)),
               threading.Thread(target=zeo.odd, args=(print_number,))]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
