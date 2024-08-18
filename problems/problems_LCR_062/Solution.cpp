//go:build ignore
#include "cpp/common/Solution.h"
#include <vector>

using namespace std;
using json = nlohmann::json;

class Trie {
private:
  vector<Trie *> children;
  bool isEnd;

  Trie *searchPrefix(string word) {
    Trie *node = this;
    for (char ch : word) {
      ch -= 'a';
      if (node->children[ch] == nullptr) {
        return nullptr;
      }
      node = node->children[ch];
    }
    return node;
  }

public:
  /** Initialize your data structure here. */
  Trie() {
    children = vector<Trie *>(26, nullptr);
    isEnd = false;
  }

  /** Inserts a word into the trie. */
  void insert(string word) {
    Trie *node = this;
    for (char ch : word) {
      if (node->children[ch - 'a'] == nullptr) {
        node->children[ch - 'a'] = new Trie();
      }
      node = node->children[ch - 'a'];
    }
    node->isEnd = true;
  }

  /** Returns if the word is in the trie. */
  bool search(string word) {
    Trie *node = searchPrefix(word);
    return node != nullptr && node->isEnd;
  }

  /** Returns if there is any word in the trie that starts with the given
   * prefix. */
  bool startsWith(string prefix) { return searchPrefix(prefix) != nullptr; }
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
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
  auto obj0 = make_shared<Trie>();
  vector<json> ans = {nullptr};
  for (size_t i = 1; i < op_values.size(); i++) {
    if (operators[i] == "insert") {
      obj0->insert(op_values[i][0]);
      ans.push_back(nullptr);
      continue;
    }
    if (operators[i] == "search") {
      ans.push_back(obj0->search(op_values[i][0]));
      continue;
    }
    if (operators[i] == "startsWith") {
      ans.push_back(obj0->startsWith(op_values[i][0]));
      continue;
    }
    ans.push_back(nullptr);
  }
  return ans;
}
