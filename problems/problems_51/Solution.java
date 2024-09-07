package problems.problems_51;

import com.alibaba.fastjson.JSON;

import java.util.*;

import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public List<List<String>> solveNQueens(int n) {
        List<List<String>> res = new ArrayList<>();
        List<List<Integer>> solutions = new ArrayList<>();
        List<Integer> path = new ArrayList<>();
        boolean[] column = new boolean[n];
        boolean[] diagonal = new boolean[2 * n];
        boolean[] antiDiagonal = new boolean[2 * n];
        Arrays.fill(column, false);
        Arrays.fill(diagonal, false);
        Arrays.fill(antiDiagonal, false);
        backtrack(n, solutions, path, column, diagonal, antiDiagonal);
        for (List<Integer> solution : solutions) {
            List<String> board = new ArrayList<>();
            for (int i = 0; i < n; i++) {
                char[] row = new char[n];
                Arrays.fill(row, '.');
                row[solution.get(i)] = 'Q';
                board.add(new String(row));
            }
            res.add(board);
        }
        return res;
    }

    private void backtrack(int n, List<List<Integer>> res, List<Integer> path, boolean[] column,
                           boolean[] diagonal, boolean[] antiDiagonal) {
        if (path.size() == n) {
            res.add(new ArrayList<>(path));
            return;
        }
        int row = path.size();
        for (int col = 0; col < n; col++) {
            if (column[col] || diagonal[row + col] || antiDiagonal[row - col + n - 1]) {
                continue;
            }
            path.add(col);
            column[col] = true;
            diagonal[row + col] = true;
            antiDiagonal[row - col + n - 1] = true;
            backtrack(n, res, path, column, diagonal, antiDiagonal);
            path.removeLast();
            column[col] = false;
            diagonal[row + col] = false;
            antiDiagonal[row - col + n - 1] = false;
        }
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int n = Integer.parseInt(inputJsonValues[0]);
        return JSON.toJSON(solveNQueens(n));
    }
}
