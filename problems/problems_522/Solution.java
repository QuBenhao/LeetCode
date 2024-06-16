package problems.problems_522;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int findLUSlength(String[] strs) {

    }

    @Override
    public Object solve(String[] values) {
        String[] strs = jsonArrayToStringArray(values[0]);
        return JSON.toJSON(findLUSlength(strs));
    }
}
