//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>> &matrix) {
        if (matrix.empty() || matrix[0].empty()) {
            return {};
        }
        vector<int> ans;
        for (int left = 0, right = matrix[0].size() - 1, top = 0, bottom = matrix.size() - 1;
             left <= right && top <= bottom; left++, right--, top++, bottom--) {
            for (int col = left; col <= right; col++) {
                ans.push_back(matrix[top][col]);
            }
            for (int row = top + 1; row <= bottom; row++) {
                ans.push_back(matrix[row][right]);
            }
            if (left < right && top < bottom) {
                for (int col = right - 1; col > left; col--) {
                    ans.push_back(matrix[bottom][col]);
                }
                for (int row = bottom; row > top; row--) {
                    ans.push_back(matrix[row][left]);
                }
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
    vector<vector<int>> matrix = json::parse(inputArray.at(0));
    return solution.spiralOrder(matrix);
}
