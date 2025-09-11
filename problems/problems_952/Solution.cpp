//go:build ignore
#include "cpp/common/Solution.h"
#include <algorithm>

using namespace std;
using json = nlohmann::json;

constexpr int MAX_N = 100000;
array<vector<int>, MAX_N + 1> PRIMES;

bool inited = false;
static void init() {
  if (inited) {
    return;
  }
  for (int i = 2; i <= MAX_N; ++i) {
    if (PRIMES[i].empty()) {
      for (int j = i; j <= MAX_N; j += i) {
        PRIMES[j].push_back(i);
      }
    }
  }
}

class UnionFind {
  vector<int> fa;
  vector<int> size;

public:
  int cc;
  explicit UnionFind(int n) : fa(n), size(n, 1), cc(n) {
    for (int i = 0; i < n; i++) {
      fa[i] = i;
    }
  }

  int find(int x) {
    if (fa[x] != x) {
      fa[x] = find(fa[x]);
    }
    return fa[x];
  }

  bool merge(int x, int y) {
    int px = find(x), py = find(y);
    if (px == py) {
      return false;
    }
    fa[px] = py;
    size[py] += size[px];
    cc--;
    return true;
  }

  int get_size(int x) { return size[find(x)]; }
};

class Solution {
public:
  int largestComponentSize(const vector<int> &nums) {
    init();
    int n = nums.size();
    UnionFind uf(n);
    unordered_map<int, int> primes_idx;
    for (int i = 0; i < n; ++i) {
      for (int p : PRIMES[nums[i]]) {
        auto it = primes_idx.find(p);
        if (it != primes_idx.end()) {
          uf.merge(i, it->second);
        }
        primes_idx[p] = i;
      }
    }
    int ans = 0;
    for (int i = 0; i < n; ++i) {
      ans = max(ans, uf.get_size(i));
    }
    return ans;
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
  return solution.largestComponentSize(nums);
}
