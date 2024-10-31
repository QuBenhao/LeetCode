package problems.problems_3259;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public long maxEnergyBoost(int[] energyDrinkA, int[] energyDrinkB) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] energyDrinkA = jsonArrayToIntArray(inputJsonValues[0]);
		int[] energyDrinkB = jsonArrayToIntArray(inputJsonValues[1]);
        return JSON.toJSON(maxEnergyBoost(energyDrinkA, energyDrinkB));
    }
}
