package problems.problems_LCR_115;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public boolean sequenceReconstruction(int[] nums, int[][] sequences) {
        Set<Integer> set = new HashSet<>();
        for (int[] seq: sequences) {
            for (int i = 0; i < seq.length - 1; i++) {
                set.add(hash(seq[i], seq[i + 1]));
            }
        }
        for (int i = 0; i < nums.length - 1; i++) {
            if (!set.contains(hash(nums[i], nums[i + 1]))) {
                return false;
            }
        }
        return true;
    }

    private int hash(int prev, int next) {
        // 10^4 最多14位
        return prev << 14 | next;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
		int[][] sequences = jsonArrayToInt2DArray(inputJsonValues[1]);
        return JSON.toJSON(sequenceReconstruction(nums, sequences));
    }
}
