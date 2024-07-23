package problems.problems_279;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    private Set<Integer> squares;
    private boolean isDividedBy(int n, int count) {
        if (count == 1) {
            return squares.contains(n);
        }
        for (int square : squares) {
            if (isDividedBy(n - square, count - 1)) {
                return true;
            }
        }
        return false;
    }
    public int numSquares(int n) {
        squares = new HashSet<>();
        for (int i = 1; i * i <= n; i++) {
            squares.add(i * i);
        }
        for (int count = 1; count <= n; count++) {
            if (isDividedBy(n, count)) {
                return count;
            }
        }
        return n;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int n = Integer.parseInt(inputJsonValues[0]);
        return JSON.toJSON(numSquares(n));
    }
}
