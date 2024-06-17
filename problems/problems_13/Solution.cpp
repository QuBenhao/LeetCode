//go:build ignore
#include "cpp/common/Solution.h"
#include <unordered_map>


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int romanToInt(string s) {
        unordered_map<char, int> romanMap = {{'I', 1},
                                             {'V', 5},
                                             {'X', 10},
                                             {'L', 50},
                                             {'C', 100},
                                             {'D', 500},
                                             {'M', 1000},};
        int ans = romanMap[s[0]], last = ans;
        int n = static_cast<int>(s.length());
        for (int i = 1; i < n; i++) {
            int v = romanMap[s[i]];
            ans += v;
            if (last < v) {
                ans -= last << 1;
            }
            last = v;
        }
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
    string s = json::parse(inputArray.at(0));
    return solution.romanToInt(s);
}
