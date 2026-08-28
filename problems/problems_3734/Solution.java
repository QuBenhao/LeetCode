package problems.problems_3734;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public String lexPalindromicPermutation(String s, String target) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String s = jsonStringToString(inputJsonValues[0]);
		String target = jsonStringToString(inputJsonValues[1]);
        return JSON.toJSON(lexPalindromicPermutation(s, target));
    }
}
