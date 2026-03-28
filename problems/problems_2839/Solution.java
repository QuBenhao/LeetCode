package problems.problems_2839;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public boolean canBeEqual(String s1, String s2) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String s1 = jsonStringToString(inputJsonValues[0]);
		String s2 = jsonStringToString(inputJsonValues[1]);
        return JSON.toJSON(canBeEqual(s1, s2));
    }
}
