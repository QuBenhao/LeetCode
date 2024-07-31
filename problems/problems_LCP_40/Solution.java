package problems.problems_LCP_40;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int maxmiumScore(int[] cards, int cnt) {

    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] cards = jsonArrayToIntArray(inputJsonValues[0]);
		int cnt = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(maxmiumScore(cards, cnt));
    }
}
