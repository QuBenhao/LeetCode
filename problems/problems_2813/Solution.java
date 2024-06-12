package problems.problems_2813;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public long findMaximumElegance(int[][] items, int k) {

    }

    @Override
    public Object solve(String[] values) {
        int[][] items = jsonArrayToInt2DArray(values[0]);
		int k = Integer.parseInt(values[1]);
        return JSON.toJSON(findMaximumElegance(items, k));
    }
}
