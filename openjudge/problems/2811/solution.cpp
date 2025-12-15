//
// Created by benhao on 2025/12/16.
//

#include <string>
#include <array>
#include <iostream>

int main() {
    std::array<std::array<int, 6>, 5> matrix{};
    for (int i = 0; i < 5; ++i) {
        for (int j = 0; j < 6; ++j) {
            std::cin >> matrix[i][j];
        }
    }
    std::array<std::array<int, 6>, 5> ans{};
    auto countStatus = [&matrix, &ans](int i, int j) -> int {
        int res = matrix[i][j] ^ ans[i][j];
        if (i > 0) {
            res ^= ans[i - 1][j];
        }
        if (j > 0) {
            res ^= ans[i][j - 1];
        }
        if (j < 5) {
            res ^= ans[i][j + 1];
        }
        return res;
    };
    for (int status = 0; status < 64; status++) {
        for (int j = 0; j < 6; ++j) {
            ans[0][j] = (status >> j) & 1;
        }
        for (int i = 1; i < 5; ++i) {
            for (int j = 0; j < 6; ++j) {
                ans[i][j] = countStatus(i - 1, j);
            }
        }
        bool valid = true;
        for (int j = 0; j < 6; ++j) {
            if (countStatus(4, j)) {
                valid = false;
                break;
            }
        }
        if (valid) {
            break;
        }
    }
    for (int i = 0; i < 5; ++i) {
        for (int j = 0; j < 5; ++j) {
            std::cout << ans[i][j] << " ";
        }
        std::cout << ans[i][5];
        if (i < 4) {
            std::cout << std::endl;
        }
    }
    std::cout << std::flush;
    return 0;
}
