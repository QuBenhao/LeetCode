//go:build ignore
#include "cpp/common/Solution.h"

#include <queue>
#include <unordered_set>


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int snakesAndLadders(vector<vector<int>>& board) {
        int n = board.size();
        queue<int> q;
        unordered_set<int> visited;
        int step = 0, target = n * n - 1;
        q.push(0);
        visited.insert(0);
        while (!q.empty()) {
            int s = q.size();
            for (int i = 0; i < s; i++) {
                int cur = q.front();
                q.pop();
                if (cur == target) {
                    return step;
                }
                bool picked = false;
                for (int j = min(target-cur, 6); j > 0; j--) {
                    int nxt = cur + j;
                    if (nxt == target) {
                        return step + 1;
                    }
                    int bi = (n - 1 - nxt / n);
                    int bj = bi % 2 == (n + 1) % 2 ? nxt % n : n - 1 - (nxt % n);
                    if (board[bi][bj] != -1) {
                        nxt = board[bi][bj] - 1;
                        if (nxt == target) {
                            return step + 1;
                        }
                    } else if (!picked) {
                        picked = true;
                    } else {
                        continue;
                    }
                    if (visited.contains(nxt)) {
                        continue;
                    }
                    visited.insert(nxt);
                    q.push(nxt);
                }
            }
            step++;
        }
        return -1;
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
	vector<vector<int>> board = json::parse(inputArray.at(0));
	return solution.snakesAndLadders(board);
}
