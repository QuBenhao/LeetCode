//
// Created by benhao on 2025/12/27.
//

#include <bits/stdc++.h>

using namespace std;

int main() {
    int n, a, b;
    cin >> n >> a >> b;
    vector<int> arr(n);
    for (int i = 0; i < n; ++i) cin >> arr[i];
    if (a == b) {
        cout << 0 << endl;
        return 0;
    }
    --a; --b;
    vector<bool> visited(n);
    visited[a] = true;
    queue<int> q;
    q.emplace(a);
    int ans = 0;
    while (!q.empty()) {
        int sz = q.size();
        ++ans;
        while (sz--) {
            int x = q.front(); q.pop();
            int hx = x + arr[x];
            if (hx == b) {
                cout << ans << endl;
                return 0;
            }
            if (hx < n && !visited[hx]) {
                visited[hx] = true;
                q.emplace(hx);
            }
            int lx = x - arr[x];
            if (lx == b) {
                cout << ans << endl;
                return 0;
            }
            if (lx >= 0 && !visited[lx]) {
                visited[lx] = true;
                q.emplace(lx);
            }
        }
    }
    cout << -1 << endl;
    return 0;
}