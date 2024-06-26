package problems.problems_2734;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public String smallestString(String s) {

    }

    @Override
    public Object solve(String[] values) {
        String s = jsonStringToString(values[0]);
        return JSON.toJSON(smallestString(s));
    }
}
