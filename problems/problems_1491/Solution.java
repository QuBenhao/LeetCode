package problems.problems_1491;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public double average(int[] salary) {
        int sum = 0, max = salary[0], min = salary[0];
        for (int v: salary) {
            sum += v;
            max = Math.max(max, v);
            min = Math.min(min, v);
        }
        return (double)(sum - max - min) / (salary.length - 2);
    }

    @Override
    public Object solve(String[] values) {
        int[] salary = jsonArrayToIntArray(values[0]);
        return JSON.toJSON(average(salary));
    }
}
