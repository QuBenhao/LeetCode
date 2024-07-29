package problems.problems_2961;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public List<Integer> getGoodIndices(int[][] variables, int target) {

    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[][] variables = jsonArrayToInt2DArray(inputJsonValues[0]);
		int target = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(getGoodIndices(variables, target));
    }
}
