package problems.problems_1;

import java.util.HashMap;

import com.alibaba.fastjson.JSON;
import qubhjava.BaseSolution;

public class Solution extends BaseSolution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer,Integer> temp = new HashMap<>();
        for(int i = 0; i < nums.length;i++){
            if(temp.containsKey(target-nums[i]))
                return new int[]{temp.get(target-nums[i]),i};
            temp.put(nums[i],i);
        }
        return null;
    }

    @Override
    public JSON solve(String input) {
        String[] values = input.split("\n");

        return JSON.toJSON(twoSum());
    }
}
