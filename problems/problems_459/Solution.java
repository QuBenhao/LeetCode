package problems.problems_459;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public boolean repeatedSubstringPattern(String s) {

    }

    @Override
    public Object solve(String[] values) {
        String s = values[0];
        return JSON.toJSON(repeatedSubstringPattern(s));
    }
}
