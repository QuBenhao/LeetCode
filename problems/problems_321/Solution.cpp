//go:build ignore
#include "cpp/common/Solution.h"

#include <algorithm>


using namespace std;
using json = nlohmann::json;

class Solution {
	deque<int> pickVector(const vector<int>& nums, int len) {
		int drop = nums.size() - len;
		deque<int> stack;
		for (int num : nums) {
			while (drop > 0 && !stack.empty() && stack.back() < num) {
				stack.pop_back();
				drop--;
			}
			stack.push_back(num);
		}
		stack.resize(len);
		return stack;
	}

	vector<int> mergeVectors(deque<int>& nums1, deque<int>& nums2) {
		vector<int> merged;
		while (!nums1.empty() || !nums2.empty()) {
			if (nums1.empty() || lexicographical_compare(nums1.begin(), nums1.end(), nums2.begin(), nums2.end())) {
				merged.push_back(nums2.front());
				nums2.pop_front();
			} else {
				merged.push_back(nums1.front());
				nums1.pop_front();
			}
		}
		return merged;
	}
public:
    vector<int> maxNumber(vector<int>& nums1, vector<int>& nums2, int k) {
		int m = nums1.size(), n = nums2.size();
		if (m > n) {
			swap(nums1, nums2);
			swap(m, n);
		}
		vector<int> result(k, 0);
		for (int i = max(0, k-n); i <= min(k, m); ++i) {
			deque<int> arr1 = pickVector(nums1, i);
			deque<int> arr2 = pickVector(nums2, k - i);
			vector<int> merged = mergeVectors(arr1, arr2);
			if (lexicographical_compare(result.begin(), result.end(), merged.begin(), merged.end())) {
				result = merged;
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
	int k = json::parse(inputArray.at(2));
	return solution.maxNumber(nums1, nums2, k);
}
