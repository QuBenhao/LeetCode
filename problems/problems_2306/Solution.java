package problems.problems_2306;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public long distinctNames(String[] ideas) {
        Set<String>[] groups = new HashSet[26];
        Arrays.setAll(groups, i -> new HashSet<>());
        for (String s : ideas) {
            groups[s.charAt(0) - 'a'].add(s.substring(1)); // Group by first letter
        }

        long ans = 0;
        for (int a = 1; a < 26; a++) { // Enumerate all pairs of groups
            for (int b = 0; b < a; b++) {
                int m = 0; // Size of the intersection
                for (String s : groups[a]) {
                    if (groups[b].contains(s)) {
                        m++;
                    }
                }
                ans += (long) (groups[a].size() - m) * (groups[b].size() - m);
            }
        }
        return ans * 2; // Multiply by 2 at the end
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String[] ideas = jsonArrayToStringArray(inputJsonValues[0]);
        return JSON.toJSON(distinctNames(ideas));
    }
}
