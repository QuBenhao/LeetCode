package problems.problems_2286;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


class BookMyShow {

    public BookMyShow(int n, int m) {

    }
    
    public int[] gather(int k, int maxRow) {

    }
    
    public boolean scatter(int k, int maxRow) {

    }
}

/**
 * Your BookMyShow object will be instantiated and called as such:
 * BookMyShow obj = new BookMyShow(n, m);
 * int[] param_1 = obj.gather(k,maxRow);
 * boolean param_2 = obj.scatter(k,maxRow);
 */

public class Solution extends BaseSolution {


    @Override
    public Object solve(String[] inputJsonValues) {
        String[] operators = jsonArrayToStringArray(inputJsonValues[0]);
		String[][] opValues = jsonArrayToString2DArray(inputJsonValues[1]);
		int n = Integer.parseInt(opValues[0][0]);
		int m = Integer.parseInt(opValues[0][1]);
		BookMyShow obj = new BookMyShow(n, m);
		List<Object> ans = new ArrayList<>(operators.length);
		ans.add(null);
		for (int i = 1; i < operators.length; i++) {
			if (operators[i].compareTo("gather") == 0) {
				int k = Integer.parseInt(opValues[i][0]);
				int maxRow = Integer.parseInt(opValues[i][1]);
				ans.add(obj.gather(k, maxRow));
				continue;
			}
			if (operators[i].compareTo("scatter") == 0) {
				int k = Integer.parseInt(opValues[i][0]);
				int maxRow = Integer.parseInt(opValues[i][1]);
				ans.add(obj.scatter(k, maxRow));
				continue;
			}
			ans.add(null);
		}
        return JSON.toJSON(ans);
    }
}
