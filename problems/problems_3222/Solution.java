package problems.problems_3222;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public String losingPlayer(int x, int y) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int x = Integer.parseInt(inputJsonValues[0]);
		int y = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(losingPlayer(x, y));
    }
}
