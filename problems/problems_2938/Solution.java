package problems.problems_2938;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public long minimumSteps(String s) {

    }

    @Override
    public Object solve(String[] values) {
        String s = values[0];
        return JSON.toJSON(minimumSteps(s));
    }
}
