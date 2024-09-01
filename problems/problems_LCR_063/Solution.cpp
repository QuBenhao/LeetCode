//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Trie {
private:
  struct TrieNode {
    vector<TrieNode *> children;
    bool isEnd;

    TrieNode() : children(26, nullptr), isEnd(false) {}
  };

  TrieNode *root;

public:
  Trie() { root = new TrieNode(); }

  void insert(string word) {
    TrieNode *node = root;
    for (char c : word) {
      if (node->children[c - 'a'] == nullptr) {
        node->children[c - 'a'] = new TrieNode();
      }
      node = node->children[c - 'a'];
    }
    node->isEnd = true;
  }

  string searchPrefix(string word) {
    TrieNode *node = root;
    string prefix;
    for (char c : word) {
      if (node->children[c - 'a'] == nullptr) {
        return word;
      }
      prefix.push_back(c);
      node = node->children[c - 'a'];
      if (node->isEnd) {
        return prefix;
      }
    }
    return word;
  }
};

class Solution {
public:
  string replaceWords(vector<string> &dictionary, string sentence) {
    Trie trie;
    for (string word : dictionary) {
      trie.insert(word);
    }
    vector<string> words;
    string word;
    for (char c : sentence) {
      if (c == ' ') {
        words.push_back(word);
        word.clear();
      } else {
        word.push_back(c);
      }
    }
    words.push_back(word);
    string result;
    for (string word : words) {
      result += trie.searchPrefix(word) + " ";
    }
    result.pop_back();
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
  vector<string> dictionary = json::parse(inputArray.at(0));
  string sentence = json::parse(inputArray.at(1));
  return solution.replaceWords(dictionary, sentence);
}
