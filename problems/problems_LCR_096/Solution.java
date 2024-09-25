package problems.problems_LCR_096;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public boolean isInterleave(String s1, String s2, String s3) {

    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String s1 = jsonStringToString(inputJsonValues[0]);
		String s2 = jsonStringToString(inputJsonValues[1]);
		String s3 = jsonStringToString(inputJsonValues[2]);
        return JSON.toJSON(isInterleave(s1, s2, s3));
    }
}
