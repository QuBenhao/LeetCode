//go:build ignore
#include "cpp/common/Solution.h"
#include <unordered_map>


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    vector<int> findIntersectionValues(vector<int>& nums1, vector<int>& nums2) {
        unordered_map<int, int> map;
        vector<int> result(2, 0);
        for (auto num: nums2) {
            map[num]++;
        }
        for (auto num: nums1) {
            if (map.find(num) != map.end()) {
                result[0]++;
                result[1] += map[num];
                map[num] = 0;
            }
        }
        return result;
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
	return solution.findIntersectionValues(nums1, nums2);
}
