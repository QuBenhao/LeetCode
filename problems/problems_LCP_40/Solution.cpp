//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int maxmiumScore(vector<int>& cards, int cnt) {
        sort(cards.begin(), cards.end(), greater<int>());
        int sum = 0;
        for (int i = 0; i < cnt; i++) {
            sum += cards[i];
        }
        if (sum % 2 == 0) {
            return sum;
        }
        auto replace_sum = [&](int x) -> int {
            for (int i = cnt; i < static_cast<int>(cards.size()); i++) {
                if (cards[i] % 2 != x % 2) {
                    return sum + cards[i] - x;
                }
            }
            return 0;
        };
        int ans = replace_sum(cards[cnt - 1]);
        for (int i = cnt - 2; i >= 0; i--) {
            if (cards[i] % 2 != cards[cnt - 1] % 2) {
                ans = max(ans, replace_sum(cards[i]));
                break;
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
	vector<int> cards = json::parse(inputArray.at(0));
	int cnt = json::parse(inputArray.at(1));
	return solution.maxmiumScore(cards, cnt);
}
