package problems.problems_2126;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public boolean asteroidsDestroyed(int mass, int[] asteroids) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int mass = Integer.parseInt(inputJsonValues[0]);
		int[] asteroids = jsonArrayToIntArray(inputJsonValues[1]);
        return JSON.toJSON(asteroidsDestroyed(mass, asteroids));
    }
}
