//go:build ignore
#include "cpp/common/Solution.h"
#include <numeric>
#include <utility>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int minStable(const vector<int> &nums, int maxC) {
    int n = nums.size();
    vector<vector<array<int, 2>>> gs(n);
    for (int i = 0; i < n; ++i) {
      vector<array<int, 2>> g;
      if (i > 0) {
        g = vector<array<int, 2>>(gs[i - 1]);
      }
      g.push_back({nums[i], i});
      int j = 0;
      for (auto& k : g) {
        k[0] = gcd(k[0], nums[i]);
        if (g[j][0] != k[0]) {
          g[++j] = k;
        }
      }
      g.resize(j+1);
      gs[i] = std::move(g);
    }

    auto check = [&nums, &gs, n, maxC](int k) {
      int count = 0;
      if (k == 0) {
        for (int i = 0; i < n; ++i) {
          if (nums[i] != 1) {
            ++count;
          }
        }
        return count <= maxC;
      }
      int i = n - 1;
      while (i >= 0) {
        bool found = false;
        for (auto it = gs[i].rbegin(); it != gs[i].rend(); ++it) {
          const auto &[v, idx] = *it;
          if (v != 1 && i - idx + 1 > k) {
            ++count;
            if (count > maxC) {
              return false;
            }
            i = max(i - k, idx) - 1;
            found = true;
            break;
          }
        }
        if (!found) {
          --i;
        }
      }
      return true;
    };

    int left = 0, right = n;
    while (left < right) {
      int mid = left + (right - left) / 2;
      if (check(mid)) {
        right = mid;
      } else {
        left = mid + 1;
      }
    }
    return left;
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
  int maxC = json::parse(inputArray.at(1));
  return solution.minStable(nums, maxC);
}
