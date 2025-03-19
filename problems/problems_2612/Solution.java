package problems.problems_2612;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int[] minReverseOperations(int n, int p, int[] banned, int k) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int n = Integer.parseInt(inputJsonValues[0]);
		int p = Integer.parseInt(inputJsonValues[1]);
		int[] banned = jsonArrayToIntArray(inputJsonValues[2]);
		int k = Integer.parseInt(inputJsonValues[3]);
        return JSON.toJSON(minReverseOperations(n, p, banned, k));
    }
}
