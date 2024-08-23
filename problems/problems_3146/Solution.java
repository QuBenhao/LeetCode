package problems.problems_3146;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int findPermutationDifference(String s, String t) {

    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String s = jsonStringToString(inputJsonValues[0]);
		String t = jsonStringToString(inputJsonValues[1]);
        return JSON.toJSON(findPermutationDifference(s, t));
    }
}
