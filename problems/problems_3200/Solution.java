package problems.problems_3200;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int maxHeightOfTriangle(int red, int blue) {
        return Math.max(f(red, blue), f(blue, red));
    }

    private int f(int n, int m) {
        int odd = (int) Math.sqrt(n);
        int even = (int) ((Math.sqrt(m * 4 + 1) - 1) / 2);
        return odd > even ? even * 2 + 1 : odd * 2;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int red = Integer.parseInt(inputJsonValues[0]);
		int blue = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(maxHeightOfTriangle(red, blue));
    }
}
