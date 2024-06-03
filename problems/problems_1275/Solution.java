package problems.problems_1275;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public String tictactoe(int[][] moves) {

    }

    @Override
    public Object solve(String[] values) {
        int[][] moves = jsonArrayToInt2DArray(values[0]);
        return JSON.toJSON(tictactoe(moves));
    }
}
