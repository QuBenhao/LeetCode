package problems.problems_2300;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int[] successfulPairs(int[] spells, int[] potions, long success) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] spells = jsonArrayToIntArray(inputJsonValues[0]);
		int[] potions = jsonArrayToIntArray(inputJsonValues[1]);
		long success = Long.parseLong(inputJsonValues[2]);
        return JSON.toJSON(successfulPairs(spells, potions, success));
    }
}
