package problems.problems_3594;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public double minTime(int n, int k, int m, int[] time, double[] mul) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int n = Integer.parseInt(inputJsonValues[0]);
		int k = Integer.parseInt(inputJsonValues[1]);
		int m = Integer.parseInt(inputJsonValues[2]);
		int[] time = jsonArrayToIntArray(inputJsonValues[3]);
		double[] mul = FIXME(inputJsonValues[4])
        return JSON.toJSON(minTime(n, k, m, time, mul));
    }
}
