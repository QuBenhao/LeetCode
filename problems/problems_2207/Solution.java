package problems.problems_2207;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public long maximumSubsequenceCount(String text, String pattern) {

    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String text = jsonStringToString(inputJsonValues[0]);
		String pattern = jsonStringToString(inputJsonValues[1]);
        return JSON.toJSON(maximumSubsequenceCount(text, pattern));
    }
}
