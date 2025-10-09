package problems.problems_3147;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int maximumEnergy(int[] energy, int k) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] energy = jsonArrayToIntArray(inputJsonValues[0]);
		int k = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(maximumEnergy(energy, k));
    }
}
