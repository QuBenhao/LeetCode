//go:build ignore
#include "cpp/common/Solution.h"
#include <numeric>


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int countBeautifulPairs(vector<int> &nums) {
        int ans = 0;
        auto counter = vector<int>(10);
        for (auto num: nums) {
            auto cur = num % 10;
            for (int i = 1; i < 10; i++) {
                if (counter[i] > 0 && gcd(cur, i) == 1) {
                    ans += counter[i];
                }
            }
            while (num >= 10) {
                num /= 10;
            }
            counter[num]++;
        }
        return ans;
    }
};

json leetcode::qubh::Solve(string input) {
    vector<string> inputArray;
    size_t pos = input.find('\n');
    while (pos != string::npos) {
        inputArray.push_back(input.substr(0, pos));
        input = input.substr(pos + 1);
        pos = input.find('\n');
    }
    inputArray.push_back(input);

    Solution solution;
    vector<int> nums = json::parse(inputArray.at(0));
    return solution.countBeautifulPairs(nums);
}
