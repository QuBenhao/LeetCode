package problems.problems_LCR_115;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public boolean sequenceReconstruction(int[] nums, int[][] sequences) {

    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
		int[][] sequences = jsonArrayToInt2DArray(inputJsonValues[1]);
        return JSON.toJSON(sequenceReconstruction(nums, sequences));
    }
}
