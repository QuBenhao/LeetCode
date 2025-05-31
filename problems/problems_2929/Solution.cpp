//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
    long long c2(long long n) {
        return n > 1 ? (n-1) * n / 2 : 0;
    }
public:
    long long distributeCandies(int n, int limit) {
        /*
         * n 个糖果分给3个人, 每个人不超过limit
         * n+2个位置放两个隔板
         * 容斥原理: 所有方案数 - C_{3}^{1} * 至少一个人超过limit + C_{3}^{2} * 至少两个人超limit - 三个人都超过limit
         * 所有方案数: C_{n+2}_{2}
         * 至少一个人超过limit: C_{n+2-(limit+1)}_{2}
         * 至少两个人超过limit: C_{n+2-2*(limit+1)}_{2}
         * 至少三个人超过limit: C_{n+2-3*(limit+1)}_{2}
        */
        return c2(n+2) - 3*c2(n+1-limit) + 3 * c2(n-2*limit) - c2(n-1-3*limit);
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
	int limit = json::parse(inputArray.at(1));
	return solution.distributeCandies(n, limit);
}
