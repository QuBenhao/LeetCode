//go:build ignore
#include "cpp/common/Solution.h"
#include <unordered_set>


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int countPrimeSetBits(int left, int right) {
        static const unordered_set<int> primes = {2, 3, 5, 7, 11, 13, 17, 19};
        int ans = 0;
        for (int i = left; i <= right; i++) {
            int count = __builtin_popcount(i);
            if (primes.find(count) != primes.end()) {
                ans++;
            }
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
	int left = json::parse(inputArray.at(0));
	int right = json::parse(inputArray.at(1));
	return solution.countPrimeSetBits(left, right);
}
