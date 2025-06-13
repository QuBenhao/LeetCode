//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class UnionFind {
    vector<int> fa;
    vector<int> size;
public:
    int cc;
    UnionFind(int n): fa(n), size(n, 1), cc(n) {
        for (int i = 0; i < n; i++) {
            fa[i] = i;
        }
    }

    int find(int x) {
        if (fa[x] != x) {
            fa[x] = find(fa[x]);
        }
        return fa[x];
    }

    bool merge(int x, int y) {
        int px = find(x), py = find(y);
        if (px == py) {
            return false;
        }
        fa[px] = py;
        size[py] += size[px];
        cc--;
        return true;
    }

    int get_size(int x) {
        return size[find(x)];
    }
};

class Solution {
public:
    vector<bool> pathExistenceQueries(int n, vector<int>& nums, int maxDiff, vector<vector<int>>& queries) {
        auto uf = UnionFind(n);
		for (int i = 0; i < n-1; ++i) {
			if (nums[i+1] - nums[i] <= maxDiff) {
				uf.merge(i, i+1);
			}
		}
		vector<bool> ans(queries.size(), false);
		for (int i = 0; i < queries.size(); ++i) {
			int u = queries[i][0], v = queries[i][1];
			ans[i] = uf.find(u) == uf.find(v);
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
	vector<int> nums = json::parse(inputArray.at(1));
	int maxDiff = json::parse(inputArray.at(2));
	vector<vector<int>> queries = json::parse(inputArray.at(3));
	return solution.pathExistenceQueries(n, nums, maxDiff, queries);
}
