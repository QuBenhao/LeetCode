package problems.problems_3720;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public String lexGreaterPermutation(String s, String target) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String s = jsonStringToString(inputJsonValues[0]);
		String target = jsonStringToString(inputJsonValues[1]);
        return JSON.toJSON(lexGreaterPermutation(s, target));
    }
}
