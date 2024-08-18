package problems.problems_551;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public boolean checkRecord(String s) {
        return !s.contains("LLL") && s.indexOf("A") == s.lastIndexOf("A");
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String s = jsonStringToString(inputJsonValues[0]);
        return JSON.toJSON(checkRecord(s));
    }
}
