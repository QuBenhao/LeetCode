package problems.problems_242;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public boolean isAnagram(String s, String t) {

    }

    @Override
    public Object solve(String[] values) {
        String s = jsonStringToString(values[0]);
		String t = jsonStringToString(values[1]);
        return JSON.toJSON(isAnagram(s, t));
    }
}
