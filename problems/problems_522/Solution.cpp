//go:build ignore
#include "cpp/common/Solution.h"
#include <iostream>


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int findLUSlength(vector<string> &strs) {
        auto is_subseq = [](const string &s, const string &t) -> bool {
            int pt_s = 0, pt_t = 0;
            while (pt_s < s.size() && pt_t < t.size()) {
                if (s[pt_s] == t[pt_t]) {
                    ++pt_s;
                }
                ++pt_t;
            }
            return pt_s == s.size();
        };

        int ans = -1;
        for (int i = 0, n = static_cast<int>(strs.size()); i < n; i++) {
            if (static_cast<int>(strs[i].size()) > ans) {
                for (int j = 0; j < n; j++) {
                    if (i != j && is_subseq(strs[i], strs[j])) {
                        goto out;
                    }
                }
                ans = static_cast<int>(strs[i].size());
                out:
            }
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
    vector<string> strs = json::parse(inputArray.at(0));
    return solution.findLUSlength(strs);
}
