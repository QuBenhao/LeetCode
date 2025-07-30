package problems.problems_2683;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public boolean doesValidArrayExist(int[] derived) {
        int a = 0;
        for (int d : derived) {
            a ^= d;
        }
        return a == 0;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] derived = jsonArrayToIntArray(inputJsonValues[0]);
        return JSON.toJSON(doesValidArrayExist(derived));
    }
}
