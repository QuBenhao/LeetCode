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

static Employee *employee_from_input(json input) {
  Employee *employee = new Employee();
  employee->id = input[0];
  employee->importance = input[1];
  vector<json> array = input[2];
  for (int v : array) {
    employee->subordinates.push_back(v);
  }
  return employee;
}

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
	vector<Employee*> employees;
	vector<json> employees_input = json::parse(inputArray.at(0));
	for (json ipt: employees_input) {
		employees.emplace_back(employee_from_input(ipt));
	}
	int id = json::parse(inputArray.at(1));
	json final_ans = solution.getImportance(employees, id);
	for (auto ptr : employees) {
		delete ptr;
	}
	employees.clear(); // Clear the vector to prevent memory leak
	return final_ans;
}
