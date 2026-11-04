package problems.problems_1385;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int findTheDistanceValue(int[] arr1, int[] arr2, int d) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] arr1 = jsonArrayToIntArray(inputJsonValues[0]);
		int[] arr2 = jsonArrayToIntArray(inputJsonValues[1]);
		int d = Integer.parseInt(inputJsonValues[2]);
        return JSON.toJSON(findTheDistanceValue(arr1, arr2, d));
    }
}
