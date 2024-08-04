//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int maxPointsInsideSquare(vector<vector<int>>& points, string s) {
        vector<int> idx_map = vector<int>(26, INT32_MAX);
        int n = static_cast<int>(points.size());
        int dis = INT32_MAX;
        for (int i = 0; i < n; i++) {
            int c = s[i] - 'a';
            int cur = max(abs(points[i][0]), abs(points[i][1]));
            if (cur < idx_map[c]) {
				dis = min(dis, idx_map[c]);
				idx_map[c] = cur;
			} else {
				dis = min(dis, cur);
            }
        }
		int ans = 0;
		for (int i = 0; i < 26; i++) {
			if (idx_map[i] < dis) {
				ans++;
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
	vector<vector<int>> points = json::parse(inputArray.at(0));
	string s = json::parse(inputArray.at(1));
	return solution.maxPointsInsideSquare(points, s);
}
