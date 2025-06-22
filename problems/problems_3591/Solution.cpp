//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

#define MAXN 100
bool inited = false, is_prime[MAXN + 1];
void init() {
  if (inited)
    return;
  inited = true;
  fill(is_prime, is_prime + MAXN + 1, true);
  is_prime[0] = is_prime[1] = false;
  for (int i = 2; i * i <= MAXN; ++i) {
    if (is_prime[i]) {
      for (int j = i * i; j <= MAXN; j += i) {
        is_prime[j] = false;
      }
    }
  }
}

class Solution {
public:
  bool checkPrimeFrequency(vector<int> &nums) {
    init();
    unordered_map<int, int> freq;
    for (int num : nums) {
      freq[num]++;
    }
    for (const auto &[_, count] : freq) {
      if (is_prime[count]) {
        return true;
      }
    }
    return false;
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
  vector<int> nums = json::parse(inputArray.at(0));
  return solution.checkPrimeFrequency(nums);
}
