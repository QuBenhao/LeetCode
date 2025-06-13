package problems.problems_1483;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


class TreeAncestor {

	int[][] pa;

    public TreeAncestor(int n, int[] parent) {
        int m = 0;
		while ((1 << m) <= n) {
			++m;
		}
		pa = new int[n][m+1];
		for (int i = 0; i < n; ++i) {
			pa[i][0] = parent[i];
		}
		for (int j = 1; j <= m; ++j) {
			for (int i = 0; i < n; ++i) {
				int p = pa[i][j-1];
				if (p == -1) {
					pa[i][j] = -1;
				} else {
					pa[i][j] = pa[p][j-1];
				}
			}
		}
    }
    
    public int getKthAncestor(int node, int k) {
        for (; k > 0 && node != -1; k &= k-1) {
			int j = Integer.numberOfTrailingZeros(k);
			node = pa[node][j];
		}
		return node;
    }
}

/**
 * Your TreeAncestor object will be instantiated and called as such:
 * TreeAncestor obj = new TreeAncestor(n, parent);
 * int param_1 = obj.getKthAncestor(node,k);
 */

public class Solution extends BaseSolution {


    @Override
    public Object solve(String[] inputJsonValues) {
        String[] operators = jsonArrayToStringArray(inputJsonValues[0]);
		String[][] opValues = jsonArrayToString2DArray(inputJsonValues[1]);
		int n = Integer.parseInt(opValues[0][0]);
		int[] parent = jsonArrayToIntArray(opValues[0][1]);
		TreeAncestor obj = new TreeAncestor(n, parent);
		List<Object> ans = new ArrayList<>(operators.length);
		ans.add(null);
		for (int i = 1; i < operators.length; i++) {
			if (operators[i].compareTo("getKthAncestor") == 0) {
				int node = Integer.parseInt(opValues[i][0]);
				int k = Integer.parseInt(opValues[i][1]);
				ans.add(obj.getKthAncestor(node, k));
				continue;
			}
			ans.add(null);
		}
        return JSON.toJSON(ans);
    }
}
