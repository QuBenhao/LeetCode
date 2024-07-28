//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int calPoints(vector<string>& operations) {
        int ans = 0;
        vector<int> arr;
        for (auto op: operations) {
            size_t n = arr.size();
            if (op == "C") {
                ans -= arr[n - 1];
                arr.pop_back();
                continue;
            }
            if (op == "+") {
                arr.emplace_back(arr[n - 2] + arr[n - 1]);
            } else if (op == "D") {
                arr.emplace_back(arr[n - 1] * 2);
            } else {
                arr.emplace_back(stoi(op, nullptr, 10));
            }
            ans += arr[n];
        }
        return ans;
    }
};

json leetcode::qubh::Solve(string input)
{
	vector<string> inputArray;
	size_t pos = input.find('\n');
	while (pos != string::npos) {
		inputArray.push_back(input.substr(0, pos));
		input = input.substr(pos + 1);
		pos = input.find('\n');
	}
	inputArray.push_back(input);

	Solution solution;
	vector<string> operations = json::parse(inputArray.at(0));
	return solution.calPoints(operations);
}
