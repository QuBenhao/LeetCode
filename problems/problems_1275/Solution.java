package problems.problems_1275;

import com.alibaba.fastjson.JSON;

import java.util.*;

import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    private boolean checkWin(int[][] moves, int[] indexes) {
        boolean meet = false;
        for (int i = 0; i < 4 && !meet; i++) {
            meet = true;
            for (int index : indexes) {
                if (i <= 1) {
                    if (moves[index][i] != moves[indexes[0]][i]) {
                        meet = false;
                        break;
                    }
                } else if (i == 2) {
                    if (moves[index][0] != moves[index][1]) {
                        meet = false;
                        break;
                    }
                } else {
                    if (moves[index][0] + moves[index][1] != 2) {
                        meet = false;
                        break;
                    }
                }
            }
        }
        return meet;
    }

    private boolean combinationCheck(int[][] moves, int start) {
        for (int i = start; i < moves.length; i += 2) {
            for (int j = i + 2; j < moves.length; j += 2) {
                for (int k = j + 2; k < moves.length; k += 2) {
                    if (checkWin(moves, new int[]{i, j, k})) {
                        return true;
                    }
                }
            }
        }
        return false;
    }

    public String tictactoe(int[][] moves) {
        if (combinationCheck(moves, 0)) {
            return "A";
        }
        if (combinationCheck(moves, 1)) {
            return "B";
        }
        return moves.length < 9 ? "Pending" : "Draw";
    }

    @Override
    public Object solve(String[] values) {
        int[][] moves = jsonArrayToInt2DArray(values[0]);
        return JSON.toJSON(tictactoe(moves));
    }
}
