//
// Created by benhao on 2025/12/19.
//
#include <iostream>

// Online judges usually use GCC
#include <bits/stdc++.h>
using namespace std;

const int MAX_A = 4e6 + 10;
const int MAX_MASK = 1 << 22;  // 2^22 > 4e6
const int FULL_MASK = (1 << 22) - 1;

int dp[MAX_MASK];

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    int n;
    cin >> n;
    vector<int> a(n);

    // Initialize the dp array to -1
    memset(dp, -1, sizeof(dp));

    // Read the numbers and mark those present
    for (int i = 0; i < n; i++) {
        cin >> a[i];
        dp[a[i]] = a[i];  // Mark the number directly
    }

    // Precompute DP: dp[mask] stores an existing number whose set bits form a subset of mask
    // Propagate from subsets to supersets
    for (int mask = 0; mask < MAX_MASK; mask++) {
        if (dp[mask] != -1) {
            // This mask itself is in the array
            continue;
        }

        // Try removing one set bit to examine a subset
        for (int i = 0; i < 22; i++) {
            if (mask & (1 << i)) {
                int sub = mask ^ (1 << i);
                if (dp[sub] != -1) {
                    dp[mask] = dp[sub];
                    break;
                }
            }
        }
    }

    // Find an answer for each a[i]
    for (int i = 0; i < n; i++) {
        // Take the complement, keeping only the lowest 22 bits
        int complement = (~a[i]) & FULL_MASK;
        cout << dp[complement] << " ";
    }

    return 0;
}
