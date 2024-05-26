package problems.problems_2028;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int[] missingRolls(int[] rolls, int mean, int n) {

    }

    @Override
    public Object solve(String[] values) {
        int[] rolls = jsonArrayToIntArray(values[0]);
		int mean = Integer.parseInt(values[1]);
		int n = Integer.parseInt(values[2]);
        return JSON.toJSON(missingRolls(rolls, mean, n));
    }
}
