package problems.problems_2894;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int differenceOfSums(int n, int m) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int n = Integer.parseInt(inputJsonValues[0]);
		int m = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(differenceOfSums(n, m));
    }
}
