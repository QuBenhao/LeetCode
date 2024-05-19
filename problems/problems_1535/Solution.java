package problems.problems_1535;

import com.alibaba.fastjson.JSON;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int getWinner(int[] arr, int k) {

    }

    @Override
    public Object solve(String[] values) {
        int[] arr = jsonArrayToIntArray(values[0]);
		int k = Integer.parseInt(values[1]);
        int res = getWinner(arr, k);
        Object obj = JSON.toJSON(res);
        System.out.println(obj);
        return obj;
    }
}
