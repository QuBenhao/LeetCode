//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class TrieNode {
public:
  TrieNode() {
    isEnd = false;
    for (int i = 0; i < 26; i++) {
      children[i] = nullptr;
    }
  }

  TrieNode *children[26];
  bool isEnd;

  bool query(string &word, int index, bool change) const {
    if (static_cast<int>(word.size()) == index) {
      return change && isEnd;
    }
    if (!change) {
      for (int i = 0; i < 26; i++) {
        if (word[index] - 'a' == i) {
          continue;
        }
        if (children[i] != nullptr &&
            children[i]->query(word, index + 1, true)) {
          return true;
        }
      }
    }
    return children[word[index] - 'a'] != nullptr &&
           children[word[index] - 'a']->query(word, index + 1, change);
  }
};

class MagicDictionary {
private:
  TrieNode *root;

public:
  /** Initialize your data structure here. */
  MagicDictionary() { root = new TrieNode(); }

  void buildDict(vector<string> dictionary) {
    for (const string &word : dictionary) {
      TrieNode *node = root;
      for (char c : word) {
        if (node->children[c - 'a'] == nullptr) {
          node->children[c - 'a'] = new TrieNode();
        }
        node = node->children[c - 'a'];
      }
      node->isEnd = true;
    }
  }

  bool search(string searchWord) { return root->query(searchWord, 0, false); }
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
