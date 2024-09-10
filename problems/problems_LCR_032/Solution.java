package problems.problems_LCR_032;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public boolean isAnagram(String s, String t) {

    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String s = jsonStringToString(inputJsonValues[0]);
		String t = jsonStringToString(inputJsonValues[1]);
        return JSON.toJSON(isAnagram(s, t));
    }
}
