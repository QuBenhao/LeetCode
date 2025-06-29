//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

struct TrieNode {
  TrieNode *children[26] = {nullptr};
  bool isEnd = false;
};

class Solution {
public:
  vector<string> partitionString(const string &s) {
    TrieNode *root = new TrieNode();
    vector<string> result;
    int start = 0;
    auto check_and_insert = [&s, &root, &result](int start) {
      TrieNode *node = root;
      for (int i = start; i < s.size(); ++i) {
        char c = s[i];
        if (node->children[c - 'a'] == nullptr) {
          result.emplace_back(s.substr(start, i - start + 1));
          node->children[c - 'a'] = new TrieNode();
          node->children[c - 'a']->isEnd = true;
          return i + 1;  // Return the next index to start from
        }
        node = node->children[c - 'a'];
      }
      return static_cast<int>(s.size());  // If we reach here, the whole string is in the trie
    };
    while (start < s.size()) {
      start = check_and_insert(start);
    }
    delete root;  // Clean up the trie
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
  string s = json::parse(inputArray.at(0));
  return solution.partitionString(s);
}
