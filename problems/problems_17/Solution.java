package problems.problems_17;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public List<String> letterCombinations(String digits) {

    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String digits = jsonStringToString(inputJsonValues[0]);
        return JSON.toJSON(letterCombinations(digits));
    }
}
