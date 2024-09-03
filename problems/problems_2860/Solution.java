package problems.problems_2860;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int countWays(List<Integer> nums) {

    }

    @Override
    public Object solve(String[] inputJsonValues) {
        List<Integer> nums = jsonArrayToIntList(inputJsonValues[0]);
        return JSON.toJSON(countWays(nums));
    }
}
