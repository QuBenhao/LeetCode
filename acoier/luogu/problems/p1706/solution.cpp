//
// Created by benhao on 2025/12/27.
//

#include <bits/stdc++.h>

using namespace std;

int n;
int path[10];
bool visited[10];

void dfs(int i) {
    if (i == n) {
        for (int j = 0; j < n; ++j) {
            cout << setw(5) << path[j];
        }
        cout << endl;
        return;
    }
    for (int j = 0; j < n; ++j) {
        if (!visited[j]) {
            visited[j] = true;
            path[i] = j + 1;
            dfs(i + 1);
            visited[j] = false;
        }
    }
}

int main() {
    cin >> n;
    dfs(0);
    return 0;
}