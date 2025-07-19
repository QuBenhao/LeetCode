//go:build ignore
#include "cpp/common/Solution.h"
#include <sstream>

using namespace std;
using json = nlohmann::json;

template <typename T>
class TrieNode {
  unordered_map<T, shared_ptr<TrieNode<T>>> children;
public:
  bool isEnd;

  TrieNode() : isEnd(false) {}
  ~TrieNode() {
    for (auto &child : children) {
      child.second.reset();
    }
  }

  template <typename Iterator>
  void insert(Iterator begin, Iterator end) {
    auto start_node = this;
    for (auto it = begin; it != end; ++it) {
      if (start_node->children.find(*it) == start_node->children.end()) {
        start_node->children[*it] = make_shared<TrieNode<T>>();
      }
      start_node = start_node->children[*it].get();
    }
    start_node->isEnd = true;
  }

  template <typename Iterator>
  bool hasPrefix(Iterator begin, Iterator end) {
    auto start_node = this;
    for (auto it = begin; it != end; ++it) {
      if (start_node->children.find(*it) == start_node->children.end()) {
        return false;
      }
      start_node = start_node->children[*it].get();
      if (start_node->isEnd) {
        return true;
      }
    }
    return false;
  }
};

class Solution {
  vector<string> split(const string &s, char delimiter) {
    stringstream ss(s);
    string item;
    vector<string> tokens;
    while (getline(ss, item, delimiter)) {
      if (!item.empty()) {
        tokens.push_back(item);
      }
    }
    return tokens;
  }

public:
  vector<string> removeSubfolders(vector<string> &folder) {
    sort(folder.begin(), folder.end(),
         [](const string &a, const string &b) { return a.size() < b.size(); });
    TrieNode<string> root;
    vector<string> result;
    for (const auto &f : folder) {
      auto parts = split(f, '/');
      if (!root.hasPrefix(parts.begin(), parts.end())) {
        result.emplace_back(f);
        root.insert(parts.begin(), parts.end());
      }
    }
    return result;
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
  vector<string> folder = json::parse(inputArray.at(0));
  return solution.removeSubfolders(folder);
}
