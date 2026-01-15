//
// Created by benhao on 2026/1/15.
// 例题: 费解的开关 acwing95
//

#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define lowbit(x) ((x)&(-(x)))

constexpr int N = 5;
uint8_t MATRIX[N];
constexpr uint8_t MASK = (1 << N) - 1;
constexpr int STEP = 6;
constexpr int DIR[4][2]{{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
int TRANS[1 << N];

int ans;

void ProcessPoint(const int x, const int y) {
    MATRIX[x] ^= 1 << (N - 1 - y);
    for (const auto& [dx, dy]: DIR) {
        const int nx = x + dx, ny = y + dy;
        if (nx < 0 || nx >= N || ny < 0 || ny >= N) continue;
        MATRIX[nx] ^= 1 << (N - 1 - ny);
    }
}

void dfs(const int r, const int s) {
    // 步数不够
    if (s > STEP || s > ans) {
        return;
    }
    if (r == N) {
        if (MATRIX[N - 1] == MASK) ans = s;
        return;
    }
    if (r == 0) {
        // 枚举每一位变或不变
        for (uint8_t i = 0; i <= MASK; ++i) {
            // 第一行，步数肯定够
            int dis = 0;
            for (int x = i; x; ) {
                int lb = lowbit(x);
                ProcessPoint(0, TRANS[lb]);
                ++dis;
                x -= lb;
            }
            dfs(r + 1, s + dis);
            for (int x = i; x; ) {
                int lb = lowbit(x);
                ProcessPoint(0, TRANS[lb]);
                x -= lb;
            }
        }
    } else {
        // 非第一行，必须把上一行全部填为1
        int dis = 0;
        const uint8_t diff = MASK ^ MATRIX[r - 1];
        for (int x = diff; x; ) {
            int lb = lowbit(x);
            ProcessPoint(r, N - 1 - TRANS[lb]);
            ++dis;
            x -= lb;
        }
        dfs(r + 1, s + dis);
        // 复原
        for (int x = diff; x; ) {
            int lb = lowbit(x);
            ProcessPoint(r, N - 1 - TRANS[lb]);
            x -= lb;
        }
    }
}

int main() {
    for (int i = 0; i < N; ++i) {
        TRANS[1 << i] = i;
    }
    int T;
    cin >> T;
    std::string line;
    while (T--) {
        for (auto & i : MATRIX) {
            cin >> line;
            i = 0;
            for (int j = 0; j < N; ++j) {
                i |= (line[j] - '0') << (N - 1 - j);
            }
        }
        ans = STEP + 1;
        dfs(0, 0);
        cout << (ans > STEP ? -1 : ans) << endl;
    }
    return 0;
}