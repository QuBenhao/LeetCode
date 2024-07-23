//go:build ignore
#include "cpp/common/Solution.h"
#include <unordered_set>


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    vector<int> relocateMarbles(vector<int>& nums, vector<int>& moveFrom, vector<int>& moveTo) {
        unordered_set<int> s(nums.begin(), nums.end());
        for (size_t i = 0; i < moveFrom.size(); i++) {
            s.erase(moveFrom[i]);
            s.insert(moveTo[i]);
        }
        vector<int> res(s.begin(), s.end());
        sort(res.begin(), res.end());
        return res;
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
	vector<int> moveFrom = json::parse(inputArray.at(1));
	vector<int> moveTo = json::parse(inputArray.at(2));
	return solution.relocateMarbles(nums, moveFrom, moveTo);
}
