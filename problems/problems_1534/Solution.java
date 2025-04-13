package problems.problems_1534;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int countGoodTriplets(int[] arr, int a, int b, int c) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] arr = jsonArrayToIntArray(inputJsonValues[0]);
		int a = Integer.parseInt(inputJsonValues[1]);
		int b = Integer.parseInt(inputJsonValues[2]);
		int c = Integer.parseInt(inputJsonValues[3]);
        return JSON.toJSON(countGoodTriplets(arr, a, b, c));
    }
}
