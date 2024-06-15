//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    vector<int> plusOne(vector<int> &digits) {
        for (int i = digits.size() - 1, cur = 1; i >= 0; i--) {
            cur += digits[i];
            digits[i] = cur % 10;
            cur /= 10;
            if (cur == 0) {
                return digits;
            }
        }
        digits.insert(digits.begin(), 1);
        return digits;
    }
};

json leetcode::qubh::Solve(string input) {
    vector<string> inputArray;
    size_t pos = input.find('\n');
    while (pos != string::npos) {
        inputArray.push_back(input.substr(0, pos));
        input = input.substr(pos + 1);
        pos = input.find('\n');
    }
    inputArray.push_back(input);

    Solution solution;
    vector<int> digits = json::parse(inputArray.at(0));
    return solution.plusOne(digits);
}
