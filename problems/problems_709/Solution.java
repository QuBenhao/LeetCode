package problems.problems_709;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public String toLowerCase(String s) {
        return s.toLowerCase();
    }

    @Override
    public Object solve(String[] values) {
        String s = jsonStringToString(values[0]);
        return JSON.toJSON(toLowerCase(s));
    }
}
