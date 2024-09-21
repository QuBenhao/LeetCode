package problems.problems_LCR_109;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int openLock(String[] deadends, String target) {

    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String[] deadends = jsonArrayToStringArray(inputJsonValues[0]);
		String target = jsonStringToString(inputJsonValues[1]);
        return JSON.toJSON(openLock(deadends, target));
    }
}
