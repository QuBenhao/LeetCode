package problems.problems_3841;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public List<Boolean> palindromePath(int n, int[][] edges, String s, String[] queries) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int n = Integer.parseInt(inputJsonValues[0]);
		int[][] edges = jsonArrayToInt2DArray(inputJsonValues[1]);
		String s = jsonStringToString(inputJsonValues[2]);
		String[] queries = jsonArrayToStringArray(inputJsonValues[3]);
        return JSON.toJSON(palindromePath(n, edges, s, queries));
    }
}
