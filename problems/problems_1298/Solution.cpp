//go:build ignore
#include "cpp/common/Solution.h"
#include <unordered_set>
#include <queue>


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int maxCandies(vector<int>& status, vector<int>& candies, vector<vector<int>>& keys, vector<vector<int>>& containedBoxes, vector<int>& initialBoxes) {
        int ans = 0;
        queue<int> q; // 可以使用的箱子
        unordered_set<int> wait; // 有箱子, 但暂时没钥匙
        for (auto b: initialBoxes) {
            if (status[b] == 1) {
                q.push(b);
            } else {
                wait.insert(b);
            }
        }
        unordered_set<int> ks;
        while (!q.empty()) {
            int box = q.front();
            q.pop();
            for (auto k: keys[box]) {
                auto it = wait.find(k);
                if (it != wait.end()) { // 先遇到了箱子, 后拿到的钥匙
                    q.push(*it);
                    wait.erase(it);
                }
                ks.insert(k);
            }
            ans += candies[box];
            for (auto b: containedBoxes[box]) {
                if (status[b] == 1 || ks.find(b) != ks.end()) { // 先拿到了钥匙, 后遇到了箱子
                    q.push(b);
                } else {
                    wait.insert(b);
                }
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
	vector<int> status = json::parse(inputArray.at(0));
	vector<int> candies = json::parse(inputArray.at(1));
	vector<vector<int>> keys = json::parse(inputArray.at(2));
	vector<vector<int>> containedBoxes = json::parse(inputArray.at(3));
	vector<int> initialBoxes = json::parse(inputArray.at(4));
	return solution.maxCandies(status, candies, keys, containedBoxes, initialBoxes);
}
