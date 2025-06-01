//go:build ignore
//
// Created by BenHao on 2025/6/1.
//

#include <functional>
#include <mutex>
#include <iostream>
#include <future>

class FooBar {
private:
    int n;
    std::mutex fooMutex, barMutex;

public:
    explicit FooBar(int n): n(n) {
        barMutex.lock();  // Start with bar locked
    }

    void foo(std::function<void()> printFoo) {
        for (int i = 0; i < n; i++) {
            fooMutex.lock();
        	// printFoo() outputs "foo". Do not change or remove this line.
        	printFoo();
            barMutex.unlock();
        }
    }

    void bar(std::function<void()> printBar) {

        for (int i = 0; i < n; i++) {
            barMutex.lock();
        	// printBar() outputs "bar". Do not change or remove this line.
        	printBar();
            fooMutex.unlock();
        }
        barMutex.unlock();
    }
};

int main() {
    // Example usage:
    FooBar fooBar(5);
    std::future<void> fooFuture = std::async(std::launch::async, [&]() { fooBar.foo([]() { std::cout << "foo"; }); });
    std::future<void> barFuture = std::async(std::launch::async, [&]() { fooBar.bar([]() { std::cout << "bar"; }); });
    fooFuture.get();
    barFuture.get();
    return 0;
}