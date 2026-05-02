package problems.problems_796;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public boolean rotateString(String s, String goal) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String s = jsonStringToString(inputJsonValues[0]);
		String goal = jsonStringToString(inputJsonValues[1]);
        return JSON.toJSON(rotateString(s, goal));
    }
}
