package problems.problems_690;

import com.alibaba.fastjson.JSON;
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
    public int getImportance(List<Employee> employees, int id) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        List<Employee> employees = FIXME(inputJsonValues[0])
		int id = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(getImportance(employees, id));
    }
}
