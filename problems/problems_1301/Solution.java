package problems.problems_1301;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int[] pathsWithMaxScore(List<String> board) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        List<String> board = jsonArrayToStringList(inputJsonValues[0]);
        return JSON.toJSON(pathsWithMaxScore(board));
    }
}
