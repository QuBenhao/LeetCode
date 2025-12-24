//
// Created by BenHao on 2025/7/6.
//
#include <iostream>

int count_odds(int a, int b) {
    int left = a + 1;
    int right = b;
    if (left > right) return 0;
    return (right + 1) / 2 - (left / 2);
}

int minimum_operations(int a, int b, int x, int y) {
    // a + 1 or a ^ 1 ( if a & 1 == 0, then a ^ 1 = a + 1; else a ^ 1 = a - 1 )
    if (a == b) {
        return 0;
    }
    if (b <= a - 1 - (a & 1)) {
        return -1;
    }
    if (b == a - 1) {
        return y;
    }
    if (x < y) {
        return x * (b - a);
    }
    // calculate odds between a+1 and b, inclusive
    int odds = count_odds(a, b);
    return odds * y + (b - a - odds) * x;
}

int main() {
    int test_cases;
    std::cin >> test_cases;
    for (int index = 0; index < test_cases; ++index) {
        int a, b, x, y;
        std::cin >> a >> b >> x >> y;
        std::cout << minimum_operations(a, b, x, y) << std::endl;
    }
    return 0;
}