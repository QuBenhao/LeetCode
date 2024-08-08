package problems.problems_2553;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int[] separateDigits(int[] nums) {
        List<Integer> ans = new ArrayList<>();
        for (int num: nums) {
            List<Integer> cur = new ArrayList<>();
            while (num > 0) {
                cur.add(num % 10);
                num /= 10;
            }
            Collections.reverse(cur);
            ans.addAll(cur);
        }
        return ans.stream().mapToInt(i -> i).toArray();
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
        return JSON.toJSON(separateDigits(nums));
    }
}
