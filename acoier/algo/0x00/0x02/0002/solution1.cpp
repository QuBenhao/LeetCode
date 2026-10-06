//
// Created by benhao on 2026/1/16.
// Example: 递归实现组合型枚举 acwing93 (non-recursive implementation)
//

#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define lowbit(x) ((x)&(-(x)))

/**
void dfs(const int cur, int remain, vector<int>& path) {
    if (remain == 0 || cur == n + 1) {
        for (const auto& v: path) cout << v << " ";
        cout << endl;
        return;
    }
    // The current element can be selected
    path.push_back(cur);
    dfs(cur + 1, remain - 1, path);
    path.pop_back();
    if (n - cur + 1 == remain) {
        // The current element cannot be skipped
        return;
    }
    // The current element can be skipped
    dfs(cur + 1, remain, path);
}

dfs(1, m, path);
 */

int st[100010], top = 0, address = 0;
void call(int x, int ret_addr) {
    int old_top = top;
    st[++top] = x; // Save the argument
    st[++top] = ret_addr; // Save the return continuation
    st[++top] = old_top; // Save the previous top
}

int ret() {
    int ret_addr = st[top - 1]; // Read the return continuation
    top = st[top]; // Restore the previous top
    return ret_addr;
}

int main() {
    int n, m;
    cin >> n >> m;
    vector<int> chosen;
    call(1, 0); // Equivalent to dfs(1)
    while (top) {
        int x = st[top - 2]; // Argument for the current computation
        switch (address) { // Split address states around the original dfs calls; two calls require three address states
            case 0: {
                if (chosen.size() > m || chosen.size() + (n - x + 1) < m) {
                    address = ret(); // Finish the computation and return
                    continue;
                }
                if (x == n + 1) {
                    for (const auto& v: chosen) cout << v << " ";
                    cout << endl;
                    address = ret();
                    continue;
                }
                chosen.push_back(x);
                call(x + 1, 1); // This return needs different handling, so its address is not 0
                address = 0; // Enter dfs(x+1) again
                continue;
            }
            case 1: {
                chosen.pop_back();
                call(x + 1, 2); // This return needs different handling, so its address is neither 0 nor 1
                address = 0; // Enter dfs(x+1) again
                continue;
            }
            case 2: {
                address = ret(); // The original final return
            }
        }
    }
    return 0;
}
