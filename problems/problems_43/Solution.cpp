//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    string multiply(string num1, string num2) {
        if (num1 == "0" || num2 == "0") {
            return "0";
        }
        auto res = vector<int>(num1.length() + num2.length());
        for (int i = num1.length() - 1; i >= 0; i--) {
            int n1 = num1[i] - '0';
            for (int j = num2.length() - 1; j >= 0; j--) {
                int n2 = num2[j] - '0';
                int cur = res[i + j + 1] + n1 * n2;
                res[i + j + 1] = cur % 10;
                res[i + j] += cur / 10;
            }
        }
        string ans;
        for (int i = res[0] == 0 ? 1 : 0; i < res.size(); i++) {
            ans.push_back('0' + res[i]);
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
	string num1 = json::parse(inputArray.at(0));
	string num2 = json::parse(inputArray.at(1));
	return solution.multiply(num1, num2);
}
