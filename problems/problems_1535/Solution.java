package problems.problems_1535;

import com.alibaba.fastjson.JSON;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int getWinner(int[] arr, int k) {
        int mx = arr[0], win = -1;
        for (int v: arr) {
            if (v > mx) {
                mx = v;
                win = 0;
            }
            if (++win == k) break;
        }
        return mx;
    }

    @Override
    public Object solve(String[] values) {
        int[] arr = jsonArrayToIntArray(values[0]);
		int k = Integer.parseInt(values[1]);
        return JSON.toJSON(getWinner(arr,k));
    }
}
