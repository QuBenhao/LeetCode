package problems.problems_2951;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public List<Integer> findPeaks(int[] mountain) {
        List<Integer> ans = new ArrayList<>();
        for (int i = 1; i < mountain.length - 1; i++) {
            if (mountain[i] > mountain[i - 1] && mountain[i] > mountain[i + 1]) {
                ans.add(i++);
            }
        }
        return ans;
    }

    @Override
    public Object solve(String[] values) {
        int[] mountain = jsonArrayToIntArray(values[0]);
        return JSON.toJSON(findPeaks(mountain));
    }
}
