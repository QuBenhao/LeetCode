//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class TrieNode {
public:
    TrieNode* children[26];
    bool isEnd;
    TrieNode() {
        for (int i = 0; i < 26; i++) {
            children[i] = nullptr;
        }
        isEnd = false;
    }

    void insert(string word) {
        TrieNode* node = this;
        for (char c : word) {
            if (node->children[c - 'a'] == nullptr) {
                node->children[c - 'a'] = new TrieNode();
            }
            node = node->children[c - 'a'];
        }
        node->isEnd = true;
    }
};

class MagicDictionary {
private:
    TrieNode* root;
    bool query(TrieNode* node, string word, size_t idx, int remain) {
        if (idx == word.size()) {
            return remain == 0 && node->isEnd;
        }
        int cur = word[idx] - 'a';
        if (node->children[cur] != nullptr) {
            if (query(node->children[cur], word, idx + 1, remain)) {
                return true;
            }
        }
        if (remain-- == 0) {
            return false;
        }
        for (int i = 0; i < 26; i++) {
            if (i == cur || node->children[i] == nullptr) {
                continue;
            }
            if (query(node->children[i], word, idx + 1, remain)) {
                return true;
            }
        }
        return false;
    }
public:
    MagicDictionary() {
        root = new TrieNode();
    }
    
    void buildDict(vector<string> dictionary) {
        for (string word : dictionary) {
            root->insert(word);
        }
    }
    
    bool search(string searchWord) {
        return query(root, searchWord, 0, 1);
    }
};

/**
 * Your MagicDictionary object will be instantiated and called as such:
 * MagicDictionary* obj = new MagicDictionary();
 * obj->buildDict(dictionary);
 * bool param_2 = obj->search(searchWord);
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
	auto obj0 = make_shared<MagicDictionary>();
	vector<json> ans = {nullptr};
	for (size_t i = 1; i < op_values.size(); i++) {
		if (operators[i] == "buildDict") {
			obj0->buildDict(op_values[i][0]);
			ans.push_back(nullptr);
			continue;
		}
		if (operators[i] == "search") {
			ans.push_back(obj0->search(op_values[i][0]));
			continue;
		}
		ans.push_back(nullptr);
	}
	return ans;
}
