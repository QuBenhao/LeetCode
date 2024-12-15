package problems.problems_1847;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int[] closestRoom(int[][] rooms, int[][] queries) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[][] rooms = jsonArrayToInt2DArray(inputJsonValues[0]);
		int[][] queries = jsonArrayToInt2DArray(inputJsonValues[1]);
        return JSON.toJSON(closestRoom(rooms, queries));
    }
}
