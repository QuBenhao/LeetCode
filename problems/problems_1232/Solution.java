package problems.problems_1232;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public boolean checkStraightLine(int[][] coordinates) {

    }

    @Override
    public Object solve(String[] values) {
        int[][] coordinates = jsonArrayToInt2DArray(values[0]);
        return JSON.toJSON(checkStraightLine(coordinates));
    }
}
