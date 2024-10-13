package problems.problems_887;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int superEggDrop(int k, int n) {

    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int k = Integer.parseInt(inputJsonValues[0]);
		int n = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(superEggDrop(k, n));
    }
}
