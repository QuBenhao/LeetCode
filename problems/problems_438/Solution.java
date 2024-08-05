package problems.problems_438;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public List<Integer> findAnagrams(String s, String p) {

    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String s = jsonStringToString(inputJsonValues[0]);
		String p = jsonStringToString(inputJsonValues[1]);
        return JSON.toJSON(findAnagrams(s, p));
    }
}
