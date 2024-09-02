package problems.problems_LCR_075;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int[] relativeSortArray(int[] arr1, int[] arr2) {

    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] arr1 = jsonArrayToIntArray(inputJsonValues[0]);
		int[] arr2 = jsonArrayToIntArray(inputJsonValues[1]);
        return JSON.toJSON(relativeSortArray(arr1, arr2));
    }
}
