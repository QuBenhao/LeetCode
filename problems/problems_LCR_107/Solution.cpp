//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    vector<vector<int>> updateMatrix(vector<vector<int>> &mat) {
        int m = static_cast<int>(mat.size()), n = static_cast<int>(mat[0].size());
        vector<vector<int>> ans(m, vector<int>(n, INT_MAX >> 1));
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (mat[i][j] == 0) {
                    ans[i][j] = 0;
                } else {
                    if (i > 0) {
                        ans[i][j] = min(ans[i][j], ans[i - 1][j] + 1);
                    }
                    if (j > 0) {
                        ans[i][j] = min(ans[i][j], ans[i][j - 1] + 1);
                    }
                }
            }
        }
        for (int i = m - 1; i >= 0; i--) {
            for (int j = n - 1; j >= 0; j--) {
                if (mat[i][j] == 0) {
                    ans[i][j] = 0;
                } else {
                    if (i < m - 1) {
                        ans[i][j] = min(ans[i][j], ans[i + 1][j] + 1);
                    }
                    if (j < n - 1) {
                        ans[i][j] = min(ans[i][j], ans[i][j + 1] + 1);
                    }
                }
            }
        }
        return ans;
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
    vector<vector<int>> mat = json::parse(inputArray.at(0));
    return solution.updateMatrix(mat);
}
