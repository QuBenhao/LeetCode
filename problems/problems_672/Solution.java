package problems.problems_672;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int flipLights(int n, int presses) {
        if (presses == 0) return 1;
        if (n == 1) return 2;
        if (n == 2) return presses == 1 ? 3 : 4;
        return presses == 1 ? 4 : presses == 2 ? 7 : 8;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int n = Integer.parseInt(inputJsonValues[0]);
		int presses = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(flipLights(n, presses));
    }
}
