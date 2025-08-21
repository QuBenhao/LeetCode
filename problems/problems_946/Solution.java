package problems.problems_946;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public boolean validateStackSequences(int[] pushed, int[] popped) {
        int n = popped.length, j = 0;
        Stack<Integer> st = new Stack<>();
        for (int x : pushed) {
            st.push(x);
            while (!st.isEmpty() && j < n && st.peek() == popped[j]) {
                st.pop();
                j++;
            }
        }
        return st.isEmpty();
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] pushed = jsonArrayToIntArray(inputJsonValues[0]);
		int[] popped = jsonArrayToIntArray(inputJsonValues[1]);
        return JSON.toJSON(validateStackSequences(pushed, popped));
    }
}
