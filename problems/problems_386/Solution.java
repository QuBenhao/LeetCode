package problems.problems_386;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public List<Integer> lexicalOrder(int n) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int n = Integer.parseInt(inputJsonValues[0]);
        return JSON.toJSON(lexicalOrder(n));
    }
}
