package problems.problems_1733;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int minimumTeachings(int n, int[][] languages, int[][] friendships) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int n = Integer.parseInt(inputJsonValues[0]);
		int[][] languages = jsonArrayToInt2DArray(inputJsonValues[1]);
		int[][] friendships = jsonArrayToInt2DArray(inputJsonValues[2]);
        return JSON.toJSON(minimumTeachings(n, languages, friendships));
    }
}
