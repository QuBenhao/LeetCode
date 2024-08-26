//go:build ignore
#include "cpp/common/Solution.h"
#include <optional>
#include <unordered_map>

using namespace std;
using json = nlohmann::json;

class Trie {
private:
  struct TrieNode {
    unordered_map<char, TrieNode *> children;
    bool isEnd = false;
  };

  TrieNode *root;

  TrieNode *searchPrefix(string word) {
    TrieNode *node = root;
    for (char ch : word) {
      if (node->children.find(ch) == node->children.end()) {
        return nullptr;
      }
      node = node->children[ch];
    }
    return node;
  }

public:
  Trie() { root = new TrieNode(); }

  void insert(string word) {
    TrieNode *node = root;
    for (char ch : word) {
      if (node->children.find(ch) == node->children.end()) {
        node->children[ch] = new TrieNode();
      }
      node = node->children[ch];
    }
    node->isEnd = true;
  }

  bool search(string word) {
    TrieNode *node = searchPrefix(word);
    return node != nullptr && node->isEnd;
  }

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
