//go:build ignore
#include "cpp/common/Solution.h"
#include <sstream>


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    string getSmallestString(string s, int k) {
        auto distance = [&](char a, char b) -> int {
            return min((a - b + 26) % 26, (b - a + 26) % 26);
        };
        stringstream ss;
        size_t idx = 0;
        while (idx < s.size() && k > 0) {
            if (s[idx] == 'a') {
                ss << 'a';
            } else {
                int d = distance(s[idx], 'a');
                if (d <= k) {
                    ss << 'a';
                    k -= d;
                } else {
                    ss << (char)(s[idx] - k);
                    k = 0;
                }
            }
            idx++;
        }
        return ss.str() + s.substr(idx);
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
    string s = json::parse(inputArray.at(0));
    int k = json::parse(inputArray.at(1));
    return solution.getSmallestString(s, k);
}
