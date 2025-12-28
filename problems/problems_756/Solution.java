package problems.problems_756;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public boolean pyramidTransition(String bottom, List<String> allowed) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String bottom = jsonStringToString(inputJsonValues[0]);
		List<String> allowed = jsonArrayToStringList(inputJsonValues[1]);
        return JSON.toJSON(pyramidTransition(bottom, allowed));
    }
}
