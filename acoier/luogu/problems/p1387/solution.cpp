//
// Created by benhao on 2025/12/17.
//

#include <iostream>
#include <vector>

int main() {
    int n, m;
    std::cin >> n >> m;
    std::vector matrix(n, std::vector<int>(m));
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            std::cin >> matrix[i][j];
        }
    }
    std::vector prefix(n + 1, std::vector<int>(m + 1));
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            prefix[i + 1][j + 1] = prefix[i + 1][j] + prefix[i][j + 1] - prefix[i][j] + matrix[i][j];
        }
    }
    int ans = 1;
    for (int i = 2; i <= n; ++i) {
        if (i <= ans) {
            continue;
        }
        for (int j = 2; j <= m; ++j) {
            if (j <= ans) {
                continue;
            }
            int d = ans;
            while (d <= std::min(i, j) && prefix[i][j] - prefix[i - d][j] - prefix[i][j - d] + prefix[i - d][j - d] == d * d) {
                ++d;
            }
            if (d - 1 > ans) {
                ans = d - 1;
                if (i <= ans) {
                    break;
                }
            }
        }
    }
    std::cout << ans << std::flush;
}