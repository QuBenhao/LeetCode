package problems.problems_3609;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int minMoves(int sx, int sy, int tx, int ty) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int sx = Integer.parseInt(inputJsonValues[0]);
		int sy = Integer.parseInt(inputJsonValues[1]);
		int tx = Integer.parseInt(inputJsonValues[2]);
		int ty = Integer.parseInt(inputJsonValues[3]);
        return JSON.toJSON(minMoves(sx, sy, tx, ty));
    }
}
