package problems.problems_950;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int[] deckRevealedIncreasing(int[] deck) {

    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] deck = jsonArrayToIntArray(inputJsonValues[0]);
        return JSON.toJSON(deckRevealedIncreasing(deck));
    }
}
