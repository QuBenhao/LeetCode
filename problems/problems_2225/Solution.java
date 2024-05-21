package problems.problems_2225;

import com.alibaba.fastjson.JSON;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public List<List<Integer>> findWinners(int[][] matches) {

    }

    @Override
    public Object solve(String[] values) {
        int[][] matches = jsonArrayToInt2DArray(values[0]);
        return JSON.toJSON(findWinners(matches));
    }
}
