package problems.problems_Interview_05__01;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int insertBits(int N, int M, int i, int j) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int N = Integer.parseInt(inputJsonValues[0]);
		int M = Integer.parseInt(inputJsonValues[1]);
		int i = Integer.parseInt(inputJsonValues[2]);
		int j = Integer.parseInt(inputJsonValues[3]);
        return JSON.toJSON(insertBits(N, M, i, j));
    }
}
