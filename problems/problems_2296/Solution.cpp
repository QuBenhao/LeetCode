//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class TextEditor {
public:
    TextEditor() {
        
    }
    
    void addText(string text) {
        
    }
    
    int deleteText(int k) {
        
    }
    
    string cursorLeft(int k) {
        
    }
    
    string cursorRight(int k) {
        
    }
};

/**
 * Your TextEditor object will be instantiated and called as such:
 * TextEditor* obj = new TextEditor();
 * obj->addText(text);
 * int param_2 = obj->deleteText(k);
 * string param_3 = obj->cursorLeft(k);
 * string param_4 = obj->cursorRight(k);
 */

json leetcode::qubh::Solve(string input_json_values) {
	vector<string> inputArray;
	size_t pos = input_json_values.find('\n');
	while (pos != string::npos) {
		inputArray.push_back(input_json_values.substr(0, pos));
		input_json_values = input_json_values.substr(pos + 1);
		pos = input_json_values.find('\n');
	}
	inputArray.push_back(input_json_values);

	vector<string> operators = json::parse(inputArray[0]);
	vector<vector<json>> op_values = json::parse(inputArray[1]);
	auto obj0 = make_shared<TextEditor>();
	vector<json> ans = {nullptr};
	for (size_t i = 1; i < op_values.size(); i++) {
		if (operators[i] == "addText") {
			obj0->addText(op_values[i][0]);
			ans.push_back(nullptr);
			continue;
		}
		if (operators[i] == "deleteText") {
			ans.push_back(obj0->deleteText(op_values[i][0]));
			continue;
		}
		if (operators[i] == "cursorLeft") {
			ans.push_back(obj0->cursorLeft(op_values[i][0]));
			continue;
		}
		if (operators[i] == "cursorRight") {
			ans.push_back(obj0->cursorRight(op_values[i][0]));
			continue;
		}
		ans.push_back(nullptr);
	}
	return ans;
}
