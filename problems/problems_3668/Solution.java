package problems.problems_3668;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int[] recoverOrder(int[] order, int[] friends) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] order = jsonArrayToIntArray(inputJsonValues[0]);
		int[] friends = jsonArrayToIntArray(inputJsonValues[1]);
        return JSON.toJSON(recoverOrder(order, friends));
    }
}
