package problems.problems_66;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int[] plusOne(int[] digits) {

    }

    @Override
    public Object solve(String[] values) {
        int[] digits = jsonArrayToIntArray(values[0]);
        return JSON.toJSON(plusOne(digits));
    }
}
