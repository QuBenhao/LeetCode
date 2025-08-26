//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  bool validSquare(const vector<int> &p1, const vector<int> &p2,
                   const vector<int> &p3, const vector<int> &p4) {
    auto distance = [](const vector<int> &point1, const vector<int> &point2) {
      return (point1[0] - point2[0]) * (point1[0] - point2[0]) +
             (point1[1] - point2[1]) * (point1[1] - point2[1]);
    };
    vector<int> distances = {distance(p1, p2), distance(p1, p3),
                             distance(p1, p4), distance(p2, p3),
                             distance(p2, p4), distance(p3, p4)};
    sort(distances.begin(), distances.end());
    return distances[0] > 0 && distances[0] == distances[1] &&
           distances[0] == distances[2] && distances[0] == distances[3] &&
           distances[4] == distances[5] && distances[4] == 2 * distances[0];
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
  vector<int> p1 = json::parse(inputArray.at(0));
  vector<int> p2 = json::parse(inputArray.at(1));
  vector<int> p3 = json::parse(inputArray.at(2));
  vector<int> p4 = json::parse(inputArray.at(3));
  return solution.validSquare(p1, p2, p3, p4);
}
