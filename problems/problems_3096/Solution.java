package problems.problems_3096;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int minimumLevels(int[] possible) {
        int s = 0;
        for (int v: possible) {
            s += v == 0 ? -1 : v;
        }
        for (int i = 0, pre = 0; i < possible.length - 1; i++) {
            pre += possible[i] == 0 ? -1 : possible[i];
            if (pre * 2 > s) {
                return i + 1;
            }
        }
        return -1;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] possible = jsonArrayToIntArray(inputJsonValues[0]);
        return JSON.toJSON(minimumLevels(possible));
    }
}
