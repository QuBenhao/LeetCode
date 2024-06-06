package problems.problems_1041;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public boolean isRobotBounded(String instructions) {

    }

    @Override
    public Object solve(String[] values) {
        String instructions = values[0];
        return JSON.toJSON(isRobotBounded(instructions));
    }
}
