package problems.problems_3609;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int minMoves(int sx, int sy, int tx, int ty) {
        if (sx == tx && sy == ty) {
            return 0; // Already at the target
        }
        if (sx > tx || sy > ty) {
            return -1; // Impossible to reach the target
        }
        int ans;
        if (tx == ty) {
            if (sx == 0) {
                ans = minMoves(sx, sy, 0, ty);
            } else {
                ans = minMoves(sx, sy, tx, 0);
            }
        } else {
            if (tx < ty) {
                int tmp = tx;
                tx = ty;
                ty = tmp;
                tmp = sx;
                sx = sy;
                sy = tmp;
            }
            if (tx > ty * 2) {
                if ((tx & 1) == 1) {
                    return -1;
                }
                ans = minMoves(sx, sy, tx / 2, ty);
            } else {
                ans = minMoves(sx, sy, tx - ty, ty);
            }
        }
        return ans == -1 ? -1 : ans + 1;
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
