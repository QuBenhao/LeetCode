package problems.problems_3248;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int finalPositionOfSnake(int n, List<String> commands) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int n = Integer.parseInt(inputJsonValues[0]);
		List<String> commands = jsonArrayToStringList(inputJsonValues[1]);
        return JSON.toJSON(finalPositionOfSnake(n, commands));
    }
}
