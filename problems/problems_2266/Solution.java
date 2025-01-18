package problems.problems_2266;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int countTexts(String pressedKeys) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String pressedKeys = jsonStringToString(inputJsonValues[0]);
        return JSON.toJSON(countTexts(pressedKeys));
    }
}
