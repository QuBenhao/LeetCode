package problems.problems_2306;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public long distinctNames(String[] ideas) {
        Set<String>[] groups = new HashSet[26];
        Arrays.setAll(groups, i -> new HashSet<>());
        for (String s : ideas) {
            groups[s.charAt(0) - 'a'].add(s.substring(1)); // 按照首字母分组
        }

        long ans = 0;
        for (int a = 1; a < 26; a++) { // 枚举所有组对
            for (int b = 0; b < a; b++) {
                int m = 0; // 交集的大小
                for (String s : groups[a]) {
                    if (groups[b].contains(s)) {
                        m++;
                    }
                }
                ans += (long) (groups[a].size() - m) * (groups[b].size() - m);
            }
        }
        return ans * 2; // 乘 2 放到最后
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String[] ideas = jsonArrayToStringArray(inputJsonValues[0]);
        return JSON.toJSON(distinctNames(ideas));
    }
}
