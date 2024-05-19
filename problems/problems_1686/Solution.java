package problems.problems_1686;

import java.util.ArrayList;

import javafx.util.Pair;

public class Solution {
    public int stoneGameVI(int[] aliceValues, int[] bobValues) {
        ArrayList<Pair<Integer, Integer>> total = new ArrayList<>();

        for (int i = 0; i < aliceValues.length; i++) {
            Pair<Integer, Integer> temp = new Pair<>(i, aliceValues[i] + bobValues[i]);
            total.add(temp);
        }

        total.sort((final Pair p1, final Pair p2) -> ((int) p2.getValue() - (int) p1.getValue()));
        int score = 0;
        boolean turn = true;
        while (!total.isEmpty()) {
            if (turn) {
                score += aliceValues[total.remove(0).getKey()];
                turn = false;
            } else {
                score -= bobValues[total.remove(0).getKey()];
                turn = true;
            }
        }
        if (score > 0)
            return 1;
        else if (score < 0)
            return -1;
        else
            return 0;
    }
}