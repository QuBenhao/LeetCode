package problems.problems_1606;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public List<Integer> busiestServers(int k, int[] arrival, int[] load) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int k = Integer.parseInt(inputJsonValues[0]);
		int[] arrival = jsonArrayToIntArray(inputJsonValues[1]);
		int[] load = jsonArrayToIntArray(inputJsonValues[2]);
        return JSON.toJSON(busiestServers(k, arrival, load));
    }
}
