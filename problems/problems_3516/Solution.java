package problems.problems_3516;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int findClosest(int x, int y, int z) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int x = Integer.parseInt(inputJsonValues[0]);
		int y = Integer.parseInt(inputJsonValues[1]);
		int z = Integer.parseInt(inputJsonValues[2]);
        return JSON.toJSON(findClosest(x, y, z));
    }
}
