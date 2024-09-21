package problems.problems_997;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int findJudge(int n, int[][] trust) {

    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int n = Integer.parseInt(inputJsonValues[0]);
		int[][] trust = jsonArrayToInt2DArray(inputJsonValues[1]);
        return JSON.toJSON(findJudge(n, trust));
    }
}
