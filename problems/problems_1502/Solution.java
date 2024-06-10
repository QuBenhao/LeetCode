package problems.problems_1502;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public boolean canMakeArithmeticProgression(int[] arr) {
        int d, n = arr.length, min = arr[0], max = arr[1];
        for (int num: arr) {
            min = Math.min(min, num);
            max = Math.max(max, num);
        }
        if (max == min) {
            return true;
        }
        if ((max - min) % (n - 1) != 0) {
            return false;
        }
        d = (max - min) / (n - 1);
        int[] explored = new int[n];
        for (int num: arr) {
            if ((num - min) % d != 0) {
                return false;
            }
            if (explored[(num - min) / d]++ > 0) {
                return false;
            }
        }
        return true;
    }

    @Override
    public Object solve(String[] values) {
        int[] arr = jsonArrayToIntArray(values[0]);
        return JSON.toJSON(canMakeArithmeticProgression(arr));
    }
}
