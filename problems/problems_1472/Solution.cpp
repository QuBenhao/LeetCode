//go:build ignore
#include "cpp/common/Solution.h"
class BrowserHistory {
public:
    BrowserHistory(string homepage) {

    }
    
    void visit(string url) {

    }
    
    string back(int steps) {

    }
    
    string forward(int steps) {

    }
};


using namespace std;
using json = nlohmann::json;

class BrowserHistory {
public:
    BrowserHistory(string homepage) {

    }
    
    void visit(string url) {

    }
    
    string back(int steps) {

    }
    
    string forward(int steps) {

    }
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



}
