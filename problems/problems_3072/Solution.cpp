//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Fenwick {
    vector<int> tree;

public:
    Fenwick(int n) : tree(n) {}

    // 把下标为 i 的元素增加 v
    void add(int i, int v) {
        while (i < tree.size()) {
            tree[i] += v;
            i += i & -i;
        }
    }

    // 返回下标在 [1,i] 的元素之和
    int pre(int i) {
        int res = 0;
        while (i > 0) {
            res += tree[i];
            i &= i - 1;
        }
        return res;
    }
};

class Solution {
public:
    vector<int> resultArray(vector<int> &nums) {
        auto sorted = nums;
        ranges::sort(sorted);
        sorted.erase(unique(sorted.begin(), sorted.end()), sorted.end());
        int m = sorted.size();

        vector<int> a{nums[0]}, b{nums[1]};
        Fenwick t(m + 1);
        t.add(sorted.end() - ranges::lower_bound(sorted, nums[0]), 1);
        t.add(sorted.end() - ranges::lower_bound(sorted, nums[1]), -1);
        for (int i = 2; i < nums.size(); i++) {
            int x = nums[i];
            int v = sorted.end() - ranges::lower_bound(sorted, x);
            int d = t.pre(v - 1); // 转换成 < v 的元素个数之差
            if (d > 0 || d == 0 && a.size() <= b.size()) {
                a.push_back(x);
                t.add(v, 1);
            } else {
                b.push_back(x);
                t.add(v, -1);
            }
        }
        a.insert(a.end(), b.begin(), b.end());
        return a;
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
	vector<int> nums = json::parse(inputArray.at(0));
	return solution.resultArray(nums);
}
