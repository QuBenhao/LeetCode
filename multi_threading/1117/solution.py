import time
from typing import Callable

import threading

class H2O:
    def __init__(self):
        self.sem_h = threading.Semaphore(2)
        self.sem_o = threading.Semaphore(1)
        self.barrier = threading.Barrier(3)

    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        self.sem_h.acquire()
        self.barrier.wait()
        # releaseHydrogen() outputs "H". Do not change or remove this line.
        releaseHydrogen()
        self.sem_h.release()

    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        self.sem_o.acquire()
        self.barrier.wait()
        # releaseOxygen() outputs "O". Do not change or remove this line.
        releaseOxygen()
        self.sem_o.release()


if __name__ == "__main__":
    h2o = H2O()
    n = 10

    def release_hydrogen():
        print("H")

    def release_oxygen():
        print("O")

    threads = []
    for i in range(n):
        threads.append(threading.Thread(target=release_oxygen))
        threads.append(threading.Thread(target=release_hydrogen))
        threads.append(threading.Thread(target=release_hydrogen))
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()