package problems.problems_3335;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int lengthAfterTransformations(String s, int t) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String s = jsonStringToString(inputJsonValues[0]);
		int t = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(lengthAfterTransformations(s, t));
    }
}
