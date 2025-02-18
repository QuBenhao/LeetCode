package problems.problems_624;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int maxDistance(List<List<Integer>> arrays) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        List<List<Integer>> arrays = jsonArrayTo2DIntList(inputJsonValues[0]);
        return JSON.toJSON(maxDistance(arrays));
    }
}
