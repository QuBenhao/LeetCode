#include <iostream>
#include <vector>

int main() {
    int n;
    std::cin >> n;
    std::vector<int> position(7, n);
    position[0] = -1;
    int ans = 0;
    int presum = 0;
    for (int i = 0; i < n; ++i) {
        int x;
        std::cin >> x;
        presum = (presum + x % 7) % 7;
        ans = std::max(ans, i - position[presum]);
        position[presum] = std::min(position[presum], i);
    }
    std::cout << ans << std::endl;
    return 0;
}