package problems.problems_762;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int countPrimeSetBits(int left, int right) {

    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int left = Integer.parseInt(inputJsonValues[0]);
		int right = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(countPrimeSetBits(left, right));
    }
}
