package problems.problems_LCR_086;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public String[][] partition(String s) {

    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String s = jsonStringToString(inputJsonValues[0]);
        return JSON.toJSON(partition(s));
    }
}
