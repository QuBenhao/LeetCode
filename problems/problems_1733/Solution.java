package problems.problems_1733;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int minimumTeachings(int n, int[][] languages, int[][] friendships) {
        int m = languages.length;
        boolean[][] lang = new boolean[m][n];
        for (int i = 0; i < m; ++i) {
            for (int l: languages[i]) {
                lang[i][l - 1] = true;
            }
        }

        Set<Integer> needs = new HashSet<>();
        out:
        for (int[] friend: friendships) {
            int u = friend[0] - 1, v = friend[1] - 1;
            for (int i = 0; i < n; ++i) {
                if (lang[u][i] && lang[v][i]) {
                    continue out;
                }
            }
            needs.add(u);
            needs.add(v);
        }
        if (needs.isEmpty()) {
            return 0;
        }
        int[] count = new int[n];
        for (int p: needs) {
            for (int i = 0; i < n; ++i) {
                if (lang[p][i]) {
                    ++count[i];
                }
            }
        }
        int mx = 0;
        for (int v: count) {
            mx = Math.max(mx, v);
        }
        return needs.size() - mx;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int n = Integer.parseInt(inputJsonValues[0]);
		int[][] languages = jsonArrayToInt2DArray(inputJsonValues[1]);
		int[][] friendships = jsonArrayToInt2DArray(inputJsonValues[2]);
        return JSON.toJSON(minimumTeachings(n, languages, friendships));
    }
}
