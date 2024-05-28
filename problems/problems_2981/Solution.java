package problems.problems_2981;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int maximumLength(String s) {

    }

    @Override
    public Object solve(String[] values) {
        String s = values[0];
        return JSON.toJSON(maximumLength(s));
    }
}
