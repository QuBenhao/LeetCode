package problems.problems_1807;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public String evaluate(String s, List<List<String>> knowledge) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String s = jsonStringToString(inputJsonValues[0]);
		List<List<String>> knowledge = jsonArrayToString2DList(inputJsonValues[1]);
        return JSON.toJSON(evaluate(s, knowledge));
    }
}
