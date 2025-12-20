package problems.problems_Interview_10__01;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public void merge(int[] A, int m, int[] B, int n) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] A = jsonArrayToIntArray(inputJsonValues[0]);
		int m = Integer.parseInt(inputJsonValues[1]);
		int[] B = jsonArrayToIntArray(inputJsonValues[2]);
		int n = Integer.parseInt(inputJsonValues[3]);
		merge(A, m, B, n);
        return JSON.toJSON(A);
    }
}
