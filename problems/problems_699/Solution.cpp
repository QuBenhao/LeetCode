//go:build ignore
#include "cpp/common/Solution.h"
#include <unordered_map>
#include <unordered_set>


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    vector<int> fallingSquares(vector<vector<int>>& positions) {
        unordered_set<int> points;
        for (auto& pos : positions) {
            points.insert(pos[0]);
            points.insert(pos[0] + pos[1] - 1);
        }
        vector<int> sorted_points(points.begin(), points.end());
        sort(sorted_points.begin(), sorted_points.end());
        int m = static_cast<int>(positions.size());
        int n = static_cast<int>(sorted_points.size());
        unordered_map<int, int> index_map;
        for (int i = 0; i < n; i++) {
            index_map[sorted_points[i]] = i;
        }
        vector<int> ans(m, 0);
        vector<int> heights(n, 0);
        int max_height = 0;
        for (int i = 0; i < m; i++) {
            auto left = index_map[positions[i][0]], height = positions[i][1];
            auto right = index_map[positions[i][0] + height - 1];
            int h = 0;
            for (int j = left; j <= right; j++) {
                h = max(h, heights[j]);
            }
            h += height;
            for (int j = left; j <= right; j++) {
                heights[j] = h;
            }
            max_height = max(max_height, h);
            ans[i] = max_height;
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
	vector<vector<int>> positions = json::parse(inputArray.at(0));
	return solution.fallingSquares(positions);
}
