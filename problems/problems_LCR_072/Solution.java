package problems.problems_LCR_072;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int mySqrt(int x) {

    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int x = Integer.parseInt(inputJsonValues[0]);
        return JSON.toJSON(mySqrt(x));
    }
}
