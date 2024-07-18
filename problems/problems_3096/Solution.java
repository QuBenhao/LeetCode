package problems.problems_3096;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int minimumLevels(int[] possible) {

    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] possible = jsonArrayToIntArray(inputJsonValues[0]);
        return JSON.toJSON(minimumLevels(possible));
    }
}
