package problems.problems_3820;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int specialNodes(int n, int[][] edges, int x, int y, int z) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int n = Integer.parseInt(inputJsonValues[0]);
		int[][] edges = jsonArrayToInt2DArray(inputJsonValues[1]);
		int x = Integer.parseInt(inputJsonValues[2]);
		int y = Integer.parseInt(inputJsonValues[3]);
		int z = Integer.parseInt(inputJsonValues[4]);
        return JSON.toJSON(specialNodes(n, edges, x, y, z));
    }
}
