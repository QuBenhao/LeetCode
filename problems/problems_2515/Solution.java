package problems.problems_2515;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int closestTarget(String[] words, String target, int startIndex) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String[] words = jsonArrayToStringArray(inputJsonValues[0]);
		String target = jsonStringToString(inputJsonValues[1]);
		int startIndex = Integer.parseInt(inputJsonValues[2]);
        return JSON.toJSON(closestTarget(words, target, startIndex));
    }
}
