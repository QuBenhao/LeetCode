//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
private:
    // 更新最大次大
    void update_max(int v, int& max1, int& max2) { // 注意这里是引用
        if (v > max1) {
            max2 = max1;
            max1 = v;
        } else if (v > max2) {
            max2 = v;
        }
    }

    // 更新最小次小
    void update_min(int v, int& min1, int& min2) { // 注意这里是引用
        if (v < min1) {
            min2 = min1;
            min1 = v;
        } else if (v < min2) {
            min2 = v;
        }
    }

public:
    int minimumDistance(vector<vector<int>>& points) {
        int max_x1 = INT_MIN, max_x2 = INT_MIN, max_y1 = INT_MIN, max_y2 = INT_MIN;
        int min_x1 = INT_MAX, min_x2 = INT_MAX, min_y1 = INT_MAX, min_y2 = INT_MAX;

        for (auto& p : points) {
            int x = p[0] + p[1];
            int y = p[1] - p[0];
            update_max(x, max_x1, max_x2);
            update_min(x, min_x1, min_x2);
            update_max(y, max_y1, max_y2);
            update_min(y, min_y1, min_y2);
        }

        int ans = INT_MAX;
        for (auto& p : points) {
            int x = p[0] + p[1];
            int y = p[1] - p[0];
            int dx = (x == max_x1 ? max_x2 : max_x1) - (x == min_x1 ? min_x2 : min_x1);
            int dy = (y == max_y1 ? max_y2 : max_y1) - (y == min_y1 ? min_y2 : min_y1);
            ans = min(ans, max(dx, dy));
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
	return solution.minimumDistance(points);
}
