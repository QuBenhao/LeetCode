package problems.problems_1884;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int twoEggDrop(int n) {
        return (int)Math.ceil(Math.sqrt(1 + 8 * n)) / 2;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int n = Integer.parseInt(inputJsonValues[0]);
        return JSON.toJSON(twoEggDrop(n));
    }
}
