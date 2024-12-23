package problems.problems_1705;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int eatenApples(int[] apples, int[] days) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] apples = jsonArrayToIntArray(inputJsonValues[0]);
		int[] days = jsonArrayToIntArray(inputJsonValues[1]);
        return JSON.toJSON(eatenApples(apples, days));
    }
}
