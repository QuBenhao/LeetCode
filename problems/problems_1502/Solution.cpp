//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    bool canMakeArithmeticProgression(vector<int>& arr) {
        int n = arr.size(), mn = arr[0], mx = arr[0];
        for (auto num: arr) {
            mn = min(mn, num); mx = max(mx, num);
        }
        if (mx == mn) {
            return true;
        }
        if ((mx - mn) % (n - 1) != 0) {
            return false;
        }
        int d = (mx - mn) / (n - 1);
        auto explored = vector<int>(n);
        for (auto num: arr) {
            if ((num - mn) % d != 0) {
                return false;
            }
            if (explored[(num - mn) / d]++ > 0) {
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
	vector<int> arr = json::parse(inputArray.at(0));
	return solution.canMakeArithmeticProgression(arr);
}
