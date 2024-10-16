package problems.problems_3193;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int numberOfPermutations(int n, int[][] requirements) {

    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int n = Integer.parseInt(inputJsonValues[0]);
		int[][] requirements = jsonArrayToInt2DArray(inputJsonValues[1]);
        return JSON.toJSON(numberOfPermutations(n, requirements));
    }
}
