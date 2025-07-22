package problems.problems_1717;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int maximumGain(String s, int x, int y) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String s = jsonStringToString(inputJsonValues[0]);
		int x = Integer.parseInt(inputJsonValues[1]);
		int y = Integer.parseInt(inputJsonValues[2]);
        return JSON.toJSON(maximumGain(s, x, y));
    }
}
