//go:build ignore
//
// Created by BenHao on 2025/6/1.
//

#include <functional>
#include <iostream>
#include <thread>
#include <barrier>
#include <semaphore>

class H2O {
private:
    std::counting_semaphore<2> hydrogenSemaphore; // Allow 2 hydrogens to proceed
    std::counting_semaphore<1> oxygenSemaphore; // Allow 1 oxygen to proceed
    std::barrier<> barrier; // Barrier for 2 hydrogens and 1 oxygen
public:
    explicit H2O(): hydrogenSemaphore(2), oxygenSemaphore(1), barrier(3) {
    }

    void hydrogen(std::function<void()> releaseHydrogen) {
        hydrogenSemaphore.acquire(); // Wait for permission to proceed
        barrier.arrive_and_wait(); // Wait for the other hydrogen and oxygen
        // releaseHydrogen() outputs "H". Do not change or remove this line.
        releaseHydrogen();
        hydrogenSemaphore.release();
    }

    void oxygen(std::function<void()> releaseOxygen) {
        oxygenSemaphore.acquire(); // Wait for permission to proceed
        barrier.arrive_and_wait(); // Wait for the two hydrogens
        // releaseOxygen() outputs "O". Do not change or remove this line.
        releaseOxygen();
        oxygenSemaphore.release();
    }
};

int main() {
    H2O h2o;
    std::thread h1([&]() {
        for (int i = 0; i < 10; i++) {
            h2o.hydrogen([]() { std::cout << "H"; });
        }
    });
    std::thread h2([&]() {
        for (int i = 0; i < 10; i++) {
            h2o.hydrogen([]() { std::cout << "H"; });
        }
    });
    std::thread o([&]() {
        for (int i = 0; i < 10; i++) {
            h2o.oxygen([]() { std::cout << "O"; });
        }
    });
    h1.detach();
    h2.detach();
    o.join();
    return 0;
}