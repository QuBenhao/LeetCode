package problems.problems_50;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public double myPow(double x, int n) {

    }

    @Override
    public Object solve(String[] values) {
        double x = FIXME(values[0])
		int n = Integer.parseInt(values[1]);
        return JSON.toJSON(myPow(x, n));
    }
}
