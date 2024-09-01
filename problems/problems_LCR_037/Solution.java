package problems.problems_LCR_037;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int[] asteroidCollision(int[] asteroids) {

    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] asteroids = jsonArrayToIntArray(inputJsonValues[0]);
        return JSON.toJSON(asteroidCollision(asteroids));
    }
}
