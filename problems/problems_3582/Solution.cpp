//go:build ignore
#include "cpp/common/Solution.h"
#include <cctype>
#include <sstream>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  string generateTag(string caption) {
    stringstream ss;
    ss << "#";
    istringstream iss(caption);
    string word;
    bool first = true;
    while (iss >> word) {
      if (word.empty())
        continue;
      if (first) {
        for (char &c : word)
          ss << static_cast<char>(tolower(c));
        first = false;
      } else {
        ss << static_cast<char>(toupper(word[0]));
        for (size_t i = 1; i < word.size(); ++i)
          ss << static_cast<char>(tolower(word[i]));
      }
    }
    string tag = ss.str();
    if (tag.length() > 100) {
      return tag.substr(0, 100);
    }
    return tag;
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
  string caption = json::parse(inputArray.at(0));
  return solution.generateTag(caption);
}
