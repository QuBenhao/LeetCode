package problems.problems_2975;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int maximizeSquareArea(int m, int n, int[] hFences, int[] vFences) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int m = Integer.parseInt(inputJsonValues[0]);
		int n = Integer.parseInt(inputJsonValues[1]);
		int[] hFences = jsonArrayToIntArray(inputJsonValues[2]);
		int[] vFences = jsonArrayToIntArray(inputJsonValues[3]);
        return JSON.toJSON(maximizeSquareArea(m, n, hFences, vFences));
    }
}
