package problems.problems_1900;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int[] earliestAndLatest(int n, int firstPlayer, int secondPlayer) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int n = Integer.parseInt(inputJsonValues[0]);
		int firstPlayer = Integer.parseInt(inputJsonValues[1]);
		int secondPlayer = Integer.parseInt(inputJsonValues[2]);
        return JSON.toJSON(earliestAndLatest(n, firstPlayer, secondPlayer));
    }
}
