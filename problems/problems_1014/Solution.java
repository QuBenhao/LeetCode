package problems.problems_1014;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int maxScoreSightseeingPair(int[] values) {

    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] values = jsonArrayToIntArray(inputJsonValues[0]);
        return JSON.toJSON(maxScoreSightseeingPair(values));
    }
}
