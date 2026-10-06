//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int longestCycle(vector<int>& edges) {
        int n = edges.size();
        int ans = -1;
        int cur_time = 1; // Current time
        vector<int> vis_time(n); // Time when x was first visited
        for (int i = 0; i < n; i++) {
            int x = i;
            int start_time = cur_time; // Start time of this traversal
            while (x != -1 && vis_time[x] == 0) { // x has not been visited
                vis_time[x] = cur_time++; // Record the time of the visit to x
                x = edges[x]; // Visit the next node
            }
            if (x != -1 && vis_time[x] >= start_time) { // Visiting x twice in this traversal means x lies on a cycle
                ans = max(ans, cur_time - vis_time[x]); // The difference between the two visit times is the cycle length
            }
        }
        return ans; // If no cycle is found, return the initial value of ans, -1
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
