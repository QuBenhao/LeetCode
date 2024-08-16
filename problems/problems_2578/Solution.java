package problems.problems_2578;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int splitNum(int num) {
        List<Integer> nums = new ArrayList<>();
        while (num > 0) {
            int r = num % 10;
            if (r != 0) {
                nums.add(r);
            }
            num /= 10;
        }
        Collections.sort(nums);
        int a = 0, b = 0;
        for (int v: nums) {
            if (a <= b) {
                a = a * 10 + v;
            } else {
                b = b * 10 + v;
            }
        }
        return a + b;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int num = Integer.parseInt(inputJsonValues[0]);
        return JSON.toJSON(splitNum(num));
    }
}
