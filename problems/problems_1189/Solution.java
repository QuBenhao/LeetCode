package problems.problems_1189;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int maxNumberOfBalloons(String text) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String text = jsonStringToString(inputJsonValues[0]);
        return JSON.toJSON(maxNumberOfBalloons(text));
    }
}
