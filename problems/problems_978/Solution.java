package problems.problems_978;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int maxTurbulenceSize(int[] arr) {
        int n = arr.length;
        int ans = 1;
        int cur0 = 1, cur1 = 1;
        for (int i = 1; i < n; i++) {
            if (arr[i] > arr[i - 1]) {
                cur1 = cur0 + 1;
                cur0 = 1;
            } else if (arr[i] < arr[i - 1]) {
                cur0 = cur1 + 1;
                cur1 = 1;
            } else {
                cur0 = 1;
                cur1 = 1;
            }
            ans = Math.max(ans, Math.max(cur0, cur1));
        }
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] arr = jsonArrayToIntArray(inputJsonValues[0]);
        return JSON.toJSON(maxTurbulenceSize(arr));
    }
}
