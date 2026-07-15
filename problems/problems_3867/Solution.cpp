//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
    static int gcd(int a, int b) {
        while (b) {
            int t = a % b;
            a = b;
            b = t;
        }
        return a;
    }
public:
    long long gcdSum(vector<int>& nums) {
        int n = nums.size();
        vector<int> pg(n);
        int mx = 0;
        for (int i = 0; i < n; i++) {
            if (nums[i] > mx) mx = nums[i];
            pg[i] = gcd(nums[i], mx);
        }
        sort(pg.begin(), pg.end());
        long long ans = 0;
        int i = 0, j = n - 1;
        while (i < j) {
            ans += gcd(pg[i], pg[j]);
            i++; j--;
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
	vector<int> nums = json::parse(inputArray.at(0));
	return solution.gcdSum(nums);
}
