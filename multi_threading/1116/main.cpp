//go:build ignore
//
// Created by BenHao on 2025/6/1.
//

#include <functional>
#include <mutex>
#include <future>
#include <iostream>

class ZeroEvenOdd {
private:
    int n;
    std::mutex zeroMutex, evenMutex, oddMutex;
public:
    explicit ZeroEvenOdd(int n): n(n) {
        oddMutex.lock();
        evenMutex.lock();
    }

    // printNumber(x) outputs "x", where x is an integer.
    void zero(std::function<void(int)> printNumber) {
        for (int i = 0; i < n; i++) {
            zeroMutex.lock();
            printNumber(0);
            if (i % 2 == 0) {
                oddMutex.unlock();
            } else {
                evenMutex.unlock();
            }
        }
    }

    void even(std::function<void(int)> printNumber) {
        for (int i = 2; i <= n; i += 2) {
            evenMutex.lock();
            printNumber(i);
            zeroMutex.unlock();
        }
    }

    void odd(std::function<void(int)> printNumber) {
        for (int i = 1; i <= n; i += 2) {
            oddMutex.lock();
            printNumber(i);
            zeroMutex.unlock();
        }
    }
};

int main() {
    ZeroEvenOdd zeroEvenOdd(5);
    std::future<void> zeroFuture = std::async(std::launch::async, [&]() { zeroEvenOdd.zero([](int x) { std::cout << x << " "; }); });
    std::future<void> evenFuture = std::async(std::launch::async, [&]() { zeroEvenOdd.even([](int x) { std::cout << x << " "; }); });
    std::future<void> oddFuture = std::async(std::launch::async, [&]() { zeroEvenOdd.odd([](int x) { std::cout << x << " "; }); });
    zeroFuture.get();
    evenFuture.get();
    oddFuture.get();
    return 0;
}