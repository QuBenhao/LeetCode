package problems.problems_3700;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int zigZagArrays(int n, int l, int r) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int n = Integer.parseInt(inputJsonValues[0]);
		int l = Integer.parseInt(inputJsonValues[1]);
		int r = Integer.parseInt(inputJsonValues[2]);
        return JSON.toJSON(zigZagArrays(n, l, r));
    }
}
