//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int minRectanglesToCoverPoints(vector<vector<int>>& points, int w) {
        sort(points.begin(), points.end());
        int ans = 0, n = static_cast<int>(points.size());
        for (int idx = 0; idx < n; ) {
            ans++;
            for (int cur = points[idx][0] + w; idx < n && points[idx][0] <= cur; idx++) {}
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
	vector<vector<int>> points = json::parse(inputArray.at(0));
	int w = json::parse(inputArray.at(1));
	return solution.minRectanglesToCoverPoints(points, w);
}
