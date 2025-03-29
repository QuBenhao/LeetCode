package problems.problems_2109;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public String addSpaces(String s, int[] spaces) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String s = jsonStringToString(inputJsonValues[0]);
		int[] spaces = jsonArrayToIntArray(inputJsonValues[1]);
        return JSON.toJSON(addSpaces(s, spaces));
    }
}
