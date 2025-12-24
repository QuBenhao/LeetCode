//
// Created by benhao on 2025/12/20.
//

#include <iostream>
#include <vector>

using namespace std;

class FenwickTree {
private:
    int n;
    vector<long long> bit1, bit2;  // 两个树状数组

    // 通用更新操作
    void update(vector<long long>& bit, int idx, long long val) {
        while (idx <= n) {
            bit[idx] += val;
            idx += idx & -idx;  // 最低位的1
        }
    }

    // 通用查询操作
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

    // 区间修改：对区间[l, r]每个元素加val
    void range_update(int l, int r, long long val) {
        update(bit1, l, val);
        update(bit1, r + 1, -val);
        update(bit2, l, val * l);
        update(bit2, r + 1, -val * (r + 1));
    }

    // 单点修改：位置idx加val
    void point_update(int idx, long long val) {
        range_update(idx, idx, val);
    }

    // 求前缀和[1, k]
    long long prefix_sum(int k) {
        return (k + 1) * query(bit1, k) - query(bit2, k);
    }

    // 区间查询：求区间[l, r]的和
    long long range_sum(int l, int r) {
        if (l > r) return 0;
        return prefix_sum(r) - prefix_sum(l - 1);
    }

    // 获取原始数组值
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