package problems.problems_LCR_001;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int divide(int a, int b) {

    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int a = Integer.parseInt(inputJsonValues[0]);
		int b = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(divide(a, b));
    }
}
