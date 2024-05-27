package problems.problems_2951;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public List<Integer> findPeaks(int[] mountain) {

    }

    @Override
    public Object solve(String[] values) {
        int[] mountain = jsonArrayToIntArray(values[0]);
        return JSON.toJSON(findPeaks(mountain));
    }
}
