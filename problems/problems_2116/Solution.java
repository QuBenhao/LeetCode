package problems.problems_2116;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public boolean canBeValid(String s, String locked) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String s = jsonStringToString(inputJsonValues[0]);
		String locked = jsonStringToString(inputJsonValues[1]);
        return JSON.toJSON(canBeValid(s, locked));
    }
}
