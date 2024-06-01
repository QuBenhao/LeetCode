package problems.problems_575;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int distributeCandies(int[] candyType) {

    }

    @Override
    public Object solve(String[] values) {
        int[] candyType = jsonArrayToIntArray(values[0]);
        return JSON.toJSON(distributeCandies(candyType));
    }
}
