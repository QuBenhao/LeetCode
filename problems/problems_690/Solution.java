package problems.problems_690;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.JSONArray;

import qubhjava.BaseSolution;

// Definition for Employee.
class Employee {
    public int id;
    public int importance;
    public List<Integer> subordinates;

    public Employee(int id, int importance, List<Integer> subordinates) {
        this.id = id;
        this.importance = importance;
        this.subordinates = subordinates;
    }
};

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
        JSONArray jsonArray = JSON.parseArray(inputJsonValues[0]);
        List<Employee> employees = new ArrayList<>(jsonArray.size());
        for (int i = 0; i < jsonArray.size(); i++) {
            JSONArray innerArray = JSON.parseArray(jsonArray.getString(i));
            employees.add(new Employee(innerArray.getIntValue(0), innerArray.getIntValue(1), jsonArrayToIntList(innerArray.getString(2))));
        }
		int id = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(getImportance(employees, id));
    }
}
