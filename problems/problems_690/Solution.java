package problems.problems_690;

import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.JSONArray;
import java.util.*;
import qubhjava.BaseSolution;

/*
// Definition for Employee.
class Employee {
    public int id;
    public int importance;
    public List<Integer> subordinates;
};
*/

public class Solution extends BaseSolution {
    private int dfs(Map<Integer, Employee> employeeMap, Employee employee) {
        int ans = employee.importance;
        for (int other: employee.subordinates) {
            ans += dfs(employeeMap, employeeMap.get(other));
        }
        return ans;
    }

    public int getImportance(List<Employee> employees, int id) {
        Map<Integer, Employee> employeeMap = new HashMap<>(employees.size());
        for (Employee e: employees) {
            employeeMap.put(e.id, e);
        }
        return dfs(employeeMap, employeeMap.get(id));
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        List<Employee> employees = Employee.Constructor(inputJsonValues[0]);
		int id = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(getImportance(employees, id));
    }
}

// Definition for Employee.
class Employee {
    public int id;
    public int importance;
    public List<Integer> subordinates;
	public static List<Employee> Constructor(String input) {
		JSONArray jsonArray = JSON.parseArray(input);
        List<Employee> employees = new ArrayList<>(jsonArray.size());
        for (int i = 0; i < jsonArray.size(); i++) {
            JSONArray innerArray = JSON.parseArray(jsonArray.getString(i));
            JSONArray subordinates = innerArray.getJSONArray(2);
            List<Integer> subordinatesList = new ArrayList<>(subordinates.size());
            for (int j = 0; j < subordinates.size(); j++) {
                subordinatesList.add(subordinates.getIntValue(j));
            }
            Employee employee = new Employee();
            employee.id = innerArray.getIntValue(0);
            employee.importance = innerArray.getIntValue(1);
            employee.subordinates = subordinatesList;
            employees.add(employee);
        }
        return employees;
	}
};
