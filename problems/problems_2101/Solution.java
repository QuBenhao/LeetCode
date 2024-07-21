package problems.problems_2101;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int maximumDetonation(int[][] bombs) {

    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[][] bombs = jsonArrayToInt2DArray(inputJsonValues[0]);
        return JSON.toJSON(maximumDetonation(bombs));
    }
}
