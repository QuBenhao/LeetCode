package problems.problems_2306;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public long distinctNames(String[] ideas) {

    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String[] ideas = jsonArrayToStringArray(inputJsonValues[0]);
        return JSON.toJSON(distinctNames(ideas));
    }
}
