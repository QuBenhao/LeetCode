//go:build ignore
#include "cpp/common/Solution.h"
#include <stack>


using namespace std;
using json = nlohmann::json;

class BrowserHistory {
public:
    BrowserHistory(string homepage) {
        b.push(homepage);
    }

    void visit(string url) {
        b.push(url);
        while (!f.empty()) {
            f.pop();
        }
    }

    string back(int steps) {
        steps = min(steps, static_cast<int>(b.size()) - 1);
        for (int i = 0; i < steps; i++) {
            f.push(std::move(b.top()));
            b.pop();
        }
        return b.top();
    }

    string forward(int steps) {
        steps = min(steps, static_cast<int>(f.size()));
        for (int i = 0; i < steps; i++) {
            b.push(f.top());
            f.pop();
        }
        return b.top();
    }
private:
    stack<string> b, f;
};

/**
 * Your BrowserHistory object will be instantiated and called as such:
 * BrowserHistory* obj = new BrowserHistory(homepage);
 * obj->visit(url);
 * string param_2 = obj->back(steps);
 * string param_3 = obj->forward(steps);
 */

json leetcode::qubh::Solve(string input) {
	vector<string> inputArray;
	size_t pos = input.find('\n');
	while (pos != string::npos) {
		inputArray.push_back(input.substr(0, pos));
		input = input.substr(pos + 1);
		pos = input.find('\n');
	}
	inputArray.push_back(input);

	vector<string> operators = json::parse(inputArray[0]);
	vector<vector<json>> values = json::parse(inputArray[1]);
	auto obj0 = make_shared<BrowserHistory>(values[0][0]);
	vector<json> ans = {nullptr};
	for (size_t i = 1; i < values.size(); i++) {
		if (operators[i] == "visit") {
			obj0->visit(values[i][0]);
			ans.push_back(nullptr);
			continue;
		}
		if (operators[i] == "back") {
			ans.push_back(obj0->back(values[i][0]));
			continue;
		}
		if (operators[i] == "forward") {
			ans.push_back(obj0->forward(values[i][0]));
			continue;
		}
	}
	return ans;
}
