package problems.problems_1;

import java.util.HashMap;

import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.JSONArray;
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
    public Object solve(String[] values) {
        JSONArray array = JSON.parseArray(values[0]);
        int[] nums = new int[array.size()];
        for (int i = 0; i < array.size(); i++) {
            nums[i] = Integer.parseInt(array.getString(i));
        }
        int target = Integer.parseInt(values[1]);
        return JSON.toJSON(twoSum(nums, target));
    }
}
