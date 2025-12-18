//
// Created by benhao on 2025/12/19.
//
#include <iostream>
#include <vector>

int main() {
    int n;
    std::cin >> n;
    std::vector<int> arr(n);
    for (int i = 0; i < n; i++) std::cin >> arr[i];
    std::sort(arr.begin(), arr.end());
    int64_t ans = 0;
    for (int i = n - 1; i >= 0; i--) {
        ans += (2ll * i - n + 1) * arr[i];
    }
    std::cout << ans * 2 << std::endl;
    return 0;
}