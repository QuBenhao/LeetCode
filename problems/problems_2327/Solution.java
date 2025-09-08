package problems.problems_2327;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int peopleAwareOfSecret(int n, int delay, int forget) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int n = Integer.parseInt(inputJsonValues[0]);
		int delay = Integer.parseInt(inputJsonValues[1]);
		int forget = Integer.parseInt(inputJsonValues[2]);
        return JSON.toJSON(peopleAwareOfSecret(n, delay, forget));
    }
}
