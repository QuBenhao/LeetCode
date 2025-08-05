package problems.problems_3477;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int numOfUnplacedFruits(int[] fruits, int[] baskets) {
        int n = fruits.length;
        int ans = 0;
        for (int fruit: fruits) {
            boolean placed = false;
            for (int i = 0; i < n; i++) {
                if (baskets[i] >= fruit) {
                    baskets[i] = 0;
                    placed = true;
                    break;
                }
            }
            if (!placed) {
                ans++;
            }
        }
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] fruits = jsonArrayToIntArray(inputJsonValues[0]);
		int[] baskets = jsonArrayToIntArray(inputJsonValues[1]);
        return JSON.toJSON(numOfUnplacedFruits(fruits, baskets));
    }
}
