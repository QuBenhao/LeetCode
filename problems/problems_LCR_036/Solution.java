package problems.problems_LCR_036;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int evalRPN(String[] tokens) {

    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String[] tokens = jsonArrayToStringArray(inputJsonValues[0]);
        return JSON.toJSON(evalRPN(tokens));
    }
}
