package problems.problems_Interview_16__04;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public String tictactoe(String[] board) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String[] board = jsonArrayToStringArray(inputJsonValues[0]);
        return JSON.toJSON(tictactoe(board));
    }
}
