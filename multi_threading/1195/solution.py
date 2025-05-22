from typing import Callable

import threading

class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.fizz_sem = threading.Semaphore(0)
        self.buzz_sem = threading.Semaphore(0)
        self.fizzbuzz_sem = threading.Semaphore(0)
        self.num_sem = threading.Semaphore(1)

    # printFizz() outputs "fizz"
    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        for i in range(self.n//3 - self.n//15):
            self.fizz_sem.acquire()
            printFizz()
            self.num_sem.release()

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        for i in range(self.n//5- self.n//15):
            self.buzz_sem.acquire()
            printBuzz()
            self.num_sem.release()

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        for i in range(self.n//15):
            self.fizzbuzz_sem.acquire()
            printFizzBuzz()
            self.num_sem.release()

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n+1):
            self.num_sem.acquire()
            match i:
                case _ if i % 3 == 0 and i % 5 == 0:
                    self.fizzbuzz_sem.release()
                case _ if i % 3 == 0:
                    self.fizz_sem.release()
                case _ if i % 5 == 0:
                    self.buzz_sem.release()
                case _:
                    printNumber(i)
                    self.num_sem.release()

if __name__ == "__main__":
    fizzbuzz = FizzBuzz(15)

    threads = [threading.Thread(target=fizzbuzz.fizz, args=(lambda: print("fizz"),)),
               threading.Thread(target=fizzbuzz.buzz, args=(lambda: print("buzz"),)),
               threading.Thread(target=fizzbuzz.number, args=(lambda x: print(x),)),
                threading.Thread(target=fizzbuzz.fizzbuzz, args=(lambda: print("fizzbuzz"),))]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
