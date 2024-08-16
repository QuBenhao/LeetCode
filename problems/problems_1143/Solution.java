package problems.problems_1143;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int longestCommonSubsequence(String text1, String text2) {

    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String text1 = jsonStringToString(inputJsonValues[0]);
		String text2 = jsonStringToString(inputJsonValues[1]);
        return JSON.toJSON(longestCommonSubsequence(text1, text2));
    }
}
