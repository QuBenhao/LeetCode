//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int candy(vector<int>& ratings) {
        int n = ratings.size();
        int ans = 0, cur = 1, top = 0, left = 0;
        for (int i = 0; i <= n; i++) { // Include i=n to ensure the final decreasing sequence is processed
            if (i == 0 || i == n || ratings[i-1] <= ratings[i]) { // Break point
                int len = i - left;
                ans += len * (len - 1)/2 + max(top, len) - top; // Contribution from the previous decreasing sequence
                if (i == 0 || i == n || ratings[i-1] == ratings[i]) {
                    cur = 1; // Reset the candy count to 1 at the break point
                } else {
                    cur++; // In an increasing sequence, use one more candy than the previous count
                }
                top = cur;
                left = i;
                ans += cur; // Accumulate the contribution from the current increasing sequence
            } else {
                cur = 1; // Currently decreasing; reset the value available for the next increasing sequence
            }
        }
        return ans-1; // Remove the extra contribution of 1 from i=n
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
