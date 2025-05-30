//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int closestMeetingNode(vector<int>& edges, int node1, int node2) {
        auto calc_dis = [&](int x) -> vector<int> {
            vector<int> dis(edges.size(), -1);
            for (int c = x, d = 0; c != -1 && dis[c] == -1; c = edges[c]) {
                dis[c] = d;
                d++;
            }
            return dis;
        };
        auto dis1 = calc_dis(node1);
        auto dis2 = calc_dis(node2);
        int ans = INT_MAX;
        int ans_idx = -1;
        int n = static_cast<int>(edges.size());
        for (int i = 0; i < n; i++) {
            if (dis1[i] == -1 || dis2[i] == -1) {
                continue;
            }
            int mx = max(dis1[i], dis2[i]);
            if (mx < ans) {
                ans = mx;
                ans_idx = i;
            }
        }
        return ans_idx;
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
	int node1 = json::parse(inputArray.at(1));
	int node2 = json::parse(inputArray.at(2));
	return solution.closestMeetingNode(edges, node1, node2);
}
