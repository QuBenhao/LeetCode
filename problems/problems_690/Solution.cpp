//go:build ignore
#include "cpp/common/Solution.h"
#include <unordered_map>

// Definition for Employee.
class Employee {
public:
  int id;
  int importance;
  vector<int> subordinates;
};

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int getImportance(vector<Employee *> employees, int id) {
    unordered_map<int, Employee *> employeeMap;
    for (Employee *employee : employees) {
      employeeMap[employee->id] = employee;
    }
    function<int(int)> dfs = [&](int id) -> int {
      Employee *employee = employeeMap[id];
      int total = employee->importance;
      for (int subordinate : employee->subordinates) {
        total += dfs(subordinate);
      }
      return total;
    };
    return dfs(id);
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
  vector<Employee *> employees;
  vector<json> employees_json = json::parse(inputArray.at(0));
  for (size_t i = 0; i < employees_json.size(); i++) {
    Employee *employee = new Employee();
    employee->id = employees_json[i][0];
    employee->importance = employees_json[i][1];
    for (size_t j = 0; j < employees_json[i][2].size(); j++) {
      employee->subordinates.push_back(employees_json[i][2][j]);
    }
    employees.push_back(employee);
  }
  int id = json::parse(inputArray.at(1));
  return solution.getImportance(employees, id);
}
