//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int candy(vector<int>& ratings) {
        int n = ratings.size();
        int ans = 0, cur = 1, top = 0, left = 0;
        for (int i = 0; i <= n; i++) { // 增加i=n的情况保证最后一个递减序列也被处理
            if (i == 0 || i == n || ratings[i-1] <= ratings[i]) { // 断点
                int len = i - left;
                ans += len * (len - 1)/2 + max(top, len) - top; // 上次递减序列的贡献
                if (i == 0 || i == n || ratings[i-1] == ratings[i]) {
                    cur = 1; // 断点重置糖果为1
                } else {
                    cur++; // 递增序列，要比上一次糖果多1
                }
                top = cur;
                left = i;
                ans += cur; // 累加当前递增序列的贡献
            } else {
                cur = 1; // 当前递减，重置下次递增可以取的值
            }
        }
        return ans-1; // 去掉i=n时的贡献1
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
	vector<int> ratings = json::parse(inputArray.at(0));
	return solution.candy(ratings);
}
