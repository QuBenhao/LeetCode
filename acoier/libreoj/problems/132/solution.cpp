//
// Created by benhao on 2025/12/20.
//

#include <iostream>
#include <vector>

using namespace std;

class FenwickTree {
private:
    int n;
    vector<long long> bit1, bit2;  // Two Fenwick trees

    // General update operation
    void update(vector<long long>& bit, int idx, long long val) {
        while (idx <= n) {
            bit[idx] += val;
            idx += idx & -idx;  // Lowest set bit
        }
    }

    // General query operation
    long long query(const vector<long long>& bit, int idx) {
        long long sum = 0;
        while (idx > 0) {
            sum += bit[idx];
            idx &= idx - 1;
        }
        return sum;
    }

public:
    FenwickTree(int size) : n(size) {
        bit1.resize(n + 1, 0);
        bit2.resize(n + 1, 0);
    }

    // Range update: add val to every element in [l, r]
    void range_update(int l, int r, long long val) {
        update(bit1, l, val);
        update(bit1, r + 1, -val);
        update(bit2, l, val * l);
        update(bit2, r + 1, -val * (r + 1));
    }

    // Point update: add val at position idx
    void point_update(int idx, long long val) {
        range_update(idx, idx, val);
    }

    // Compute the prefix sum [1, k]
    long long prefix_sum(int k) {
        return (k + 1) * query(bit1, k) - query(bit2, k);
    }

    // Range query: compute the sum of [l, r]
    long long range_sum(int l, int r) {
        if (l > r) return 0;
        return prefix_sum(r) - prefix_sum(l - 1);
    }

    // Get the original array value
    long long get_value(int idx) {
        return range_sum(idx, idx);
    }
};

int main() {
    int n, q;
    std::cin >> n >> q;
    FenwickTree tree(n);
    for (int i = 0; i < n; i++) {
        int val;
        std::cin >> val;
        tree.point_update(i + 1, val);
    }
    for (int i = 0; i < q; i++) {
        int ty, l, r;
        std::cin >> ty;
        if (ty == 1) {
            int64_t v;
            std::cin >> l >> r >> v;
            tree.range_update(l, r, v);
        } else {
            std::cin >> l >> r;
            std::cout << tree.range_sum(l, r) << std::endl;
        }
    }
    return 0;
}
