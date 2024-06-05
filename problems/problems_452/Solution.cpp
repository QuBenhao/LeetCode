//go:build ignore
#include "cpp/common/Solution.h"
#include <ranges>
#include <algorithm>


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int findMinArrowShots(vector<vector<int>>& points) {
        std::ranges::sort(points, [](const vector<int>& a, const vector<int>& b) {
            return a[1] < b[1];
        });
        int cur = points[0][1], ans = 1;
        for (auto point: points) {
            if (point[0] > cur) {
                ans++;
                cur = point[1];
            }
        }
        return ans;
    }
};

json leetcode::qubh::Solve(string input)
{
	vector<string> inputArray;
	size_t pos = input.find('\n');
	while (pos != string::npos) {
		inputArray.push_back(input.substr(0, pos));
		input = input.substr(pos + 1);
		pos = input.find('\n');
	}
	inputArray.push_back(input);

	Solution solution;
	vector<vector<int>> points = json::parse(inputArray.at(0));
	return solution.findMinArrowShots(points);
}
