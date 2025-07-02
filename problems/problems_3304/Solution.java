package problems.problems_3304;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public char kthCharacter(int k) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int k = Integer.parseInt(inputJsonValues[0]);
        return JSON.toJSON(kthCharacter(k));
    }
}
