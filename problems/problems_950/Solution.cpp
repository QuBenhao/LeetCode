//go:build ignore
#include "cpp/common/Solution.h"
#include <deque>


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    vector<int> deckRevealedIncreasing(vector<int>& deck) {
        deque<int> ans;
        sort(deck.begin(), deck.end());
        for (auto i = static_cast<int>(deck.size()) - 1; i >= 0; --i) {
            if (!ans.empty()) {
                int last = ans.back();
				ans.pop_back();
				ans.push_front(last);
            }
			ans.push_front(deck[i]);
        }
		return vector<int>(ans.begin(), ans.end());
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
	vector<int> deck = json::parse(inputArray.at(0));
	return solution.deckRevealedIncreasing(deck);
}
