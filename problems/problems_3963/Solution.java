package problems.problems_3963;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public String[] createGrid(int m, int n) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int m = Integer.parseInt(inputJsonValues[0]);
		int n = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(createGrid(m, n));
    }
}
