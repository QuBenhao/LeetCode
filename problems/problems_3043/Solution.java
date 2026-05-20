package problems.problems_3043;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int longestCommonPrefix(int[] arr1, int[] arr2) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] arr1 = jsonArrayToIntArray(inputJsonValues[0]);
		int[] arr2 = jsonArrayToIntArray(inputJsonValues[1]);
        return JSON.toJSON(longestCommonPrefix(arr1, arr2));
    }
}
