//go:build ignore
#include "cpp/common/Solution.h"
#include <stdint.h>


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    double myPow(double x, int n) {
        if (x == 0.0) {
            return 0.0;
        }
        double ans = 1.0;
        if (n < 0) {
            x = 1.0/x;
            if (n == INT32_MIN) {
                ans = x;
                n = INT32_MAX;
            } else {
                n = -n;
            }
        }
        while (n > 0) {
            if ((n & 1) == 1) {
                ans *= x;
            }
            x *= x;
            n >>= 1;
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
	double x = json::parse(inputArray.at(0));
	int n = json::parse(inputArray.at(1));
	return solution.myPow(x, n);
}
