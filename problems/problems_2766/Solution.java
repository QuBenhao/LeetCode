package problems.problems_2766;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public List<Integer> relocateMarbles(int[] nums, int[] moveFrom, int[] moveTo) {
        Set<Integer> set = new HashSet<>();
        for (int num : nums) {
            set.add(num);
        }
        for (int i = 0; i < moveFrom.length; i++) {
            set.remove(moveFrom[i]);
            set.add(moveTo[i]);
        }
        List<Integer> res = new ArrayList<>(set);
        Collections.sort(res);
        return res;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
        int[] moveFrom = jsonArrayToIntArray(inputJsonValues[1]);
        int[] moveTo = jsonArrayToIntArray(inputJsonValues[2]);
        return JSON.toJSON(relocateMarbles(nums, moveFrom, moveTo));
    }
}
