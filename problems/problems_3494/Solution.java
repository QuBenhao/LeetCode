package problems.problems_3494;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public long minTime(int[] skill, int[] mana) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] skill = jsonArrayToIntArray(inputJsonValues[0]);
		int[] mana = jsonArrayToIntArray(inputJsonValues[1]);
        return JSON.toJSON(minTime(skill, mana));
    }
}
