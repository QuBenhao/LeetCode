package problems.problems_LCR_075;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int[] relativeSortArray(int[] arr1, int[] arr2) {
        int mx = 0;
        for (int x : arr1) {
            mx = Math.max(mx, x);
        }
        int[] frequency = new int[mx + 1];
        for (int x : arr1) {
            frequency[x]++;
        }
        int[] ans = new int[arr1.length];
        int index = 0;
        for (int x : arr2) {
            for (int i = 0; i < frequency[x]; i++) {
                ans[index++] = x;
            }
            frequency[x] = 0;
        }
        for (int x = 0; x <= mx; x++) {
            for (int i = 0; i < frequency[x]; i++) {
                ans[index++] = x;
            }
        }
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] arr1 = jsonArrayToIntArray(inputJsonValues[0]);
		int[] arr2 = jsonArrayToIntArray(inputJsonValues[1]);
        return JSON.toJSON(relativeSortArray(arr1, arr2));
    }
}
