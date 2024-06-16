//go:build ignore
#include "cpp/common/Solution.h"
#include <queue>


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    string addBinary(string a, string b) {
        string ans;
        if (b.length() > a.length()) {
            swap(a, b);
        }
        int cur = 0, m = a.length(), n = b.length();
        for (int i = n - 1; i >= 0; i--) {
            cur += a[i + m - n] - '0' + b[i] - '0';
            ans.push_back(cur % 2 ? '1' : '0');
            cur >>= 1;
        }
        for (int i = m - n - 1; i >= 0; i--) {
            cur += a[i] - '0';
            ans.push_back(cur % 2 ? '1' : '0');
            cur >>= 1;
        }
        if (cur > 0) {
            ans.push_back('1');
        }
        std::reverse(ans.begin(), ans.end());
        return ans;
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
    string a = json::parse(inputArray.at(0));
    string b = json::parse(inputArray.at(1));
    return solution.addBinary(a, b);
}
