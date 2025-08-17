package problems.problems_3648;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int minSensors(int n, int m, int k) {
        k = 2 * k + 1;
        return ((m - 1) / k + 1) * ((n - 1) / k + 1);
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int n = Integer.parseInt(inputJsonValues[0]);
		int m = Integer.parseInt(inputJsonValues[1]);
		int k = Integer.parseInt(inputJsonValues[2]);
        return JSON.toJSON(minSensors(n, m, k));
    }
}
