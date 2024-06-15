//go:build ignore
#include "cpp/common/Solution.h"
#include <algorithm>


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    double average(vector<int>& salary) {
        int s = 0, mx = salary[0], mn = salary[0];
        for (auto v: salary) {
            s += v;
            mx = max(mx, v);
            mn = min(mn, v);
        }
        return (double)(s - mx - mn) / (double)(salary.size() - 2);
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
	vector<int> salary = json::parse(inputArray.at(0));
	return solution.average(salary);
}
