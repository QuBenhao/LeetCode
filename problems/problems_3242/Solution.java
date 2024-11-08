package problems.problems_3242;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


class NeighborSum {

    public NeighborSum(int[][] grid) {
        
    }
    
    public int adjacentSum(int value) {
        
    }
    
    public int diagonalSum(int value) {
        
    }
}

/**
 * Your NeighborSum object will be instantiated and called as such:
 * NeighborSum obj = new NeighborSum(grid);
 * int param_1 = obj.adjacentSum(value);
 * int param_2 = obj.diagonalSum(value);
 */

public class Solution extends BaseSolution {


    @Override
    public Object solve(String[] inputJsonValues) {
        String[] operators = jsonArrayToStringArray(inputJsonValues[0]);
		String[][] opValues = jsonArrayToString2DArray(inputJsonValues[1]);
		int[][] grid = jsonArrayToInt2DArray(opValues[0][0]);
		NeighborSum obj = new NeighborSum(grid);
		List<Object> ans = new ArrayList<>(operators.length);
		ans.add(null);
		for (int i = 1; i < operators.length; i++) {
			if (operators[i].compareTo("adjacentSum") == 0) {
				int value = Integer.parseInt(opValues[i][0]);
				ans.add(obj.adjacentSum(value));
				continue;
			}
			if (operators[i].compareTo("diagonalSum") == 0) {
				int value = Integer.parseInt(opValues[i][0]);
				ans.add(obj.diagonalSum(value));
				continue;
			}
			ans.add(null);
		}
        return JSON.toJSON(ans);
    }
}
