package problems.problems_1542;

import com.alibaba.fastjson.JSON;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int longestAwesome(String s) {

    }

    @Override
    public Object solve(String[] values) {
        String s = values[0];
        return JSON.toJSON(longestAwesome(s));
    }
}
