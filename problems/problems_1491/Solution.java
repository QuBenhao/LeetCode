package problems.problems_1491;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public double average(int[] salary) {

    }

    @Override
    public Object solve(String[] values) {
        int[] salary = jsonArrayToIntArray(values[0]);
        return JSON.toJSON(average(salary));
    }
}
