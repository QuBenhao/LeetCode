//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Fenwick {
    vector<int> tree;

public:
    Fenwick(int n) : tree(n) {}

    // Increase the element at index i by v
    void add(int i, int v) {
        while (i < tree.size()) {
            tree[i] += v;
            i += i & -i;
        }
    }

    // Return the sum of the elements at indices [1,i]
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
            int d = t.pre(v - 1); // Convert to the difference in the counts of elements < v
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
