//
// Created by benhao on 2026/1/1.
//

#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int n;
vector<int> arr, pa;
unordered_map<int, vector<int>> graph;

pair<int, int> dfs(const int node) {
    int with = arr[node], without = 0;
    for (const auto& child: graph[node]) {
        const auto&[w, wn] = dfs(child);
        if (w > 0) {
            without += max(w, wn);
        }
        if (wn > 0) {
            with += wn;
        }
    }
    return {with, without};
}

int main() {
    cin >> n;
    arr.resize(n);
    pa.resize(n);
    graph.clear();
    bool all_neg = true;
    int max_val = INT_MIN;
    for (int i = 0; i < n; ++i) {
        cin >> arr[i];
        if (arr[i] >= 0) {
            all_neg = false;
        }
        max_val = max(max_val, arr[i]);
        pa[i] = -1;
    }
    for (int i = 0; i < n - 1; ++i) {
        int l, k;
        cin >> l >> k;
        pa[l - 1] = k - 1;
        graph[k - 1].emplace_back(l - 1);
    }
    if (all_neg) {
        cout << max_val << endl;
        return 0;
    }
    int root = 0;
    for (int i = 0; i < n; ++i) {
        if (pa[i] == -1) {
            root = i;
            break;
        }
    }
    auto ans = dfs(root);
    cout << max(ans.first, ans.second) << endl;
    return 0;
}