//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    bool lemonadeChange(vector<int>& bills) {
        int fives = 0, tens = 0;
        for (auto bill: bills) {
            if (bill == 5) {
                fives++;
            } else if (bill == 10) {
                tens++;
                fives--;
            } else if (tens > 0) {
                tens--;
                fives--;
            } else {
                fives -= 3;
            }
            if (fives < 0) {
                return false;
            }
        }
        return true;
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
	vector<int> bills = json::parse(inputArray.at(0));
	return solution.lemonadeChange(bills);
}
