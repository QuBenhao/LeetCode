//go:build ignore
//
// Created by BenHao on 2025/6/1.
//

#include <iostream>
#include <mutex>
#include <functional>
#include <future>

using namespace std;

class Foo {
    mutex second_lock, third_lock;
public:
    explicit Foo() {
        second_lock.lock();
        third_lock.lock();
    }

    void first(function<void()> printFirst) {
        // printFirst() outputs "first". Do not change or remove this line.
        printFirst();
        second_lock.unlock();
    }

    void second(function<void()> printSecond) {
        second_lock.lock();
        // printSecond() outputs "second". Do not change or remove this line.
        printSecond();
        second_lock.unlock();
        third_lock.unlock();
    }

    void third(function<void()> printThird) {
        third_lock.lock();
        // printThird() outputs "third". Do not change or remove this line.
        printThird();
        third_lock.unlock();
    }
};

int main() {
    Foo foo;
    auto f1 = async(launch::async, [&]() { foo.first([]() { cout << "first" << endl; }); });
    auto f2 = async(launch::async, [&]() { foo.second([]() { cout << "second" << endl; }); });
    auto f3 = async(launch::async, [&]() { foo.third([]() { cout << "third" << endl; }); });
    f1.get();
    f2.get();
    f3.get();
    return 0;
}