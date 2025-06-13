//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int countCoveredBuildings(int n, vector<vector<int>>& buildings) {
        vector<array<int, 2>> bound_x(n+1, {n+1, -1}), bound_y(n+1, {n+1, -1});
		for (const auto& building : buildings) {
			int x = building[0], y = building[1];
			bound_x[x][0] = min(bound_x[x][0], y);
			bound_x[x][1] = max(bound_x[x][1], y);
			bound_y[y][0] = min(bound_y[y][0], x);
			bound_y[y][1] = max(bound_y[y][1], x);
		}
		int ans = 0;
		for (const auto& building : buildings) {
			int x = building[0], y = building[1];
			if (bound_x[x][0] < y && bound_x[x][1] > y &&
			    bound_y[y][0] < x && bound_y[y][1] > x) {
				++ans;
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
	int n = json::parse(inputArray.at(0));
	vector<vector<int>> buildings = json::parse(inputArray.at(1));
	return solution.countCoveredBuildings(n, buildings);
}
