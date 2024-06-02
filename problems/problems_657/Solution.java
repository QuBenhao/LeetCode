package problems.problems_657;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public boolean judgeCircle(String moves) {
        int horizontal = 0, vertical = 0;
        for (int i = 0; i < moves.length(); i++) {
            switch (moves.charAt(i)) {
                case 'L':
                    horizontal--;
                    break;
                case 'U':
                    vertical++;
                    break;
                case 'D':
                    vertical--;
                    break;
                default:
                    horizontal++;
            }
        }
        return horizontal == 0 && vertical == 0;
    }

    @Override
    public Object solve(String[] values) {
        String moves = values[0];
        return JSON.toJSON(judgeCircle(moves));
    }
}
