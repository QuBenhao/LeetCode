//
// Created by benhao on 2026/1/24.
// Example: IncDec Sequence acwing100
//

#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define lowbit(x) ((x)&(-(x)))

int main() {
    int n;
    std::cin >> n;
    long long cur;
    std::cin >> cur;
    /**
     * One operation can apply diff[l]++, diff[r+1]-- or diff[l]--, diff[r+1]++
     * Find the minimum number of operations to make diff[1] ~ diff[n - 1] all 0
     * Also find the range of possible values of diff[0]
     *
     * Positive and negative values cancel: +1 and -1 cancel once, while -2 and +2 cancel twice. The remaining positive or negative surplus determines the range of diff[0]
     * The surplus can be paired with changes to either diff[0] or diff[n], so each surplus unit may or may not change diff[0]
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
