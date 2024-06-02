package problems.problems_657;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public boolean judgeCircle(String moves) {

    }

    @Override
    public Object solve(String[] values) {
        String moves = values[0];
        return JSON.toJSON(judgeCircle(moves));
    }
}
