package problems.problems_3582;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public String generateTag(String caption) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String caption = jsonStringToString(inputJsonValues[0]);
        return JSON.toJSON(generateTag(caption));
    }
}
