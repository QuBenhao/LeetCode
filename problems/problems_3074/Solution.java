package problems.problems_3074;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int minimumBoxes(int[] apple, int[] capacity) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] apple = jsonArrayToIntArray(inputJsonValues[0]);
		int[] capacity = jsonArrayToIntArray(inputJsonValues[1]);
        return JSON.toJSON(minimumBoxes(apple, capacity));
    }
}
