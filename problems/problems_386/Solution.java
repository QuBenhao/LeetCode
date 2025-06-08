package problems.problems_386;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public List<Integer> lexicalOrder(int n) {
        List<Integer> ans = new ArrayList<>(n);
        for (int i = 0, j = 1; i < n; i++) {
            ans.add(j);
            if (j * 10 <= n) {
                j *= 10; // Go to the next level
            } else {
                while (j % 10 == 9 || j + 1 > n) {
                    j /= 10; // Backtrack to the previous level
                }
                j++; // Move to the next number at the current level
            }
        }
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int n = Integer.parseInt(inputJsonValues[0]);
        return JSON.toJSON(lexicalOrder(n));
    }
}
