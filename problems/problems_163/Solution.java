package problems.problems_163;

import com.alibaba.fastjson.JSON;

import java.util.*;

import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public List<List<Integer>> findMissingRanges(int[] nums, int lower, int upper) {
        int last = lower - 1;
        List<List<Integer>> ans = new ArrayList<>();
        for (int num : nums) {
            if (num - last > 1) {
                List<Integer> tmp = new ArrayList<>(2);
                tmp.add(last + 1);
                tmp.add(num - 1);
                ans.add(tmp);
            }
            last = num;
        }
        if (upper > last) {
            ans.add(new ArrayList<>(2) {{
                add(nums.length > 0 ? nums[nums.length - 1] + 1 : lower);
                add(upper);
            }});
        }
        return ans;
    }

    @Override
    public Object solve(String[] values) {
        int[] nums = jsonArrayToIntArray(values[0]);
        int lower = Integer.parseInt(values[1]);
        int upper = Integer.parseInt(values[2]);
        return JSON.toJSON(findMissingRanges(nums, lower, upper));
    }
}
