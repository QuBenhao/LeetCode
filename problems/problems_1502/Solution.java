package problems.problems_1502;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public boolean canMakeArithmeticProgression(int[] arr) {

    }

    @Override
    public Object solve(String[] values) {
        int[] arr = jsonArrayToIntArray(values[0]);
        return JSON.toJSON(canMakeArithmeticProgression(arr));
    }
}
