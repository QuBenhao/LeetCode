package problems.problems_LCR_098;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int uniquePaths(int m, int n) {

    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int m = Integer.parseInt(inputJsonValues[0]);
		int n = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(uniquePaths(m, n));
    }
}
