package problems.problems_1592;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public String reorderSpaces(String text) {
        int space = 0, n = text.length();
        List<String> words = new ArrayList<>();
        for (int i = 0, start = -1; i <= n; ++i) {
            if (i == n || text.charAt(i) == ' ') {
                if (start != -1) {
                    words.add(text.substring(start, i));
                    start = -1;
                }
                if (i < n) {
                    ++space;
                }
            } else if (start == -1) {
                start = i;
            }
        }
        int m = words.size();
        if (m == 1) {
            return words.get(0) + " ".repeat(space);
        }
        int d = space / (m - 1), r = space % (m - 1);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < m; ++i) {
            sb.append(words.get(i));
            if (i < m - 1) {
                sb.append(" ".repeat(d));
            }
        }
        if (r > 0) {
            sb.append(" ".repeat(r));
        }
        return sb.toString();
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String text = jsonStringToString(inputJsonValues[0]);
        return JSON.toJSON(reorderSpaces(text));
    }
}
