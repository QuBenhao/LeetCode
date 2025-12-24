//
// Created by benhao on 2025/12/22.
//

#include <iostream>

int main() {
    int n;
    std::cin >> n;
    long long cur;
    std::cin >> cur;
    /**
     * 一次操作中，我们可以使 diff[l]++, diff[r+1]-- 或者 diff[l]--, diff[r+1]++
     * 求使diff[1] ~ diff[n - 1]全为0的最小操作次数
     * 并求diff[0]的取值范围
     *
     * 正负可以抵消, 比如正1和负1就消除一次，负2和正2就消除两次，最后看正的多出的或者负的多出的，就是diff[0]的取值范围
     * 因为多出来的部分可以选择和diff[0]变化或者和diff[n]变化, 也就是多出来的部分diff[0]可以变也可以不变
     */
    long long positive = 0LL, negative = 0LL;
    for (int i = 1; i < n; ++i) {
        long long v;
        std::cin >> v;
        long long d = v - cur;
        if (d < 0) {
            negative -= d;
        } else if (d > 0) {
            positive += d;
        }
        cur = v;
    }
    std::cout << std::max(positive, negative) << std::endl;
    std::cout << (positive > negative ? positive - negative : negative - positive) + 1 << std::endl;
    return 0;
}