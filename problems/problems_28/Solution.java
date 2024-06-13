package problems.problems_28;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int strStr(String haystack, String needle) {
        return haystack.indexOf(needle);
    }

    @Override
    public Object solve(String[] values) {
        String haystack = jsonStringToString(values[0]);
		String needle = jsonStringToString(values[1]);
        return JSON.toJSON(strStr(haystack, needle));
    }
}
