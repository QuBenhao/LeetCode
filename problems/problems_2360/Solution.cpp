//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int longestCycle(vector<int>& edges) {
        int n = edges.size();
        int ans = -1;
        int cur_time = 1; // 当前时间
        vector<int> vis_time(n); // 首次访问 x 的时间
        for (int i = 0; i < n; i++) {
            int x = i;
            int start_time = cur_time; // 本轮循环的开始时间
            while (x != -1 && vis_time[x] == 0) { // 没有访问过 x
                vis_time[x] = cur_time++; // 记录访问 x 的时间
                x = edges[x]; // 访问下一个节点
            }
            if (x != -1 && vis_time[x] >= start_time) { // x 在本轮循环中访问了两次，说明 x 在环上
                ans = max(ans, cur_time - vis_time[x]); // 前后两次访问 x 的时间差，即为环长
            }
        }
        return ans; // 如果没有找到环，返回的是 ans 的初始值 -1
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
	vector<int> edges = json::parse(inputArray.at(0));
	return solution.longestCycle(edges);
}
