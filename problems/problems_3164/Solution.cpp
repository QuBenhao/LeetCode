//go:build ignore
#include "cpp/common/Solution.h"
#include <unordered_map>


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    long long numberOfPairs(vector<int>& nums1, vector<int>& nums2, int k) {
        unordered_map<int, int> cnt1;
        for (int x : nums1) {
            if (x % k == 0) {
                cnt1[x / k]++;
            }
        }
        if (cnt1.empty()) {
            return 0;
        }

        unordered_map<int, int> cnt2;
        for (int x : nums2) {
            cnt2[x]++;
        }

        long long ans = 0;
        int u = ranges::max_element(cnt1)->first;
        for (auto& [x, cnt] : cnt2) {
            int s = 0;
            for (int y = x; y <= u; y += x) { // 枚举 x 的倍数
                s += cnt1.contains(y) ? cnt1[y] : 0;
            }
            ans += (long long) s * cnt;
        }
        return ans;
    }
};

json leetcode::qubh::Solve(string input_json_values) {
	vector<string> inputArray;
	size_t pos = input_json_values.find('\n');
	while (pos != string::npos) {
		inputArray.push_back(input_json_values.substr(0, pos));
		input_json_values = input_json_values.substr(pos + 1);
		pos = input_json_values.find('\n');
	}
	inputArray.push_back(input_json_values);

	Solution solution;
	vector<int> nums1 = json::parse(inputArray.at(0));
	vector<int> nums2 = json::parse(inputArray.at(1));
	int k = json::parse(inputArray.at(2));
	return solution.numberOfPairs(nums1, nums2, k);
}
