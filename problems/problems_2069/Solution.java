package problems.problems_2069;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


class Robot {
	private static final String[] DIRS = {"East", "North", "West", "South"};
	private final int m, n, total;
	private int loc;
	private boolean moved;

    public Robot(int width, int height) {
        this.m = width;
        this.n = height;
        this.total = 2 * (width + height - 2);
        this.loc = 0;
        this.moved = false;
    }
    
    public void step(int num) {
        num %= total;
        loc = (loc + num) % total;
        moved = true;
    }
    
    public int[] getPos() {
        int[] mv = move();
		return new int[]{mv[0], mv[1]};
    }
    
    public String getDir() {
        return DIRS[move()[2]];
    }

	private int[] move() {
		if (!moved) {
			return new int[]{0, 0, 0};
		}
		if (loc < m) {
			return new int[]{loc, 0, loc == 0 ? 3 : 0};
		}
		if (loc < m + n - 1) {
			return new int[]{m - 1, loc - m + 1, 1};
		}
		if (loc < 2 * m + n - 2) {
			return new int[]{m - 1 - (loc - m - n + 2), n - 1, 2};
		}
		return new int[]{0, total - loc, 3};
	}
}

/**
 * Your Robot object will be instantiated and called as such:
 * Robot obj = new Robot(width, height);
 * obj.step(num);
 * int[] param_2 = obj.getPos();
 * String param_3 = obj.getDir();
 */

public class Solution extends BaseSolution {


    @Override
    public Object solve(String[] inputJsonValues) {
        String[] operators = jsonArrayToStringArray(inputJsonValues[0]);
		String[][] opValues = jsonArrayToString2DArray(inputJsonValues[1]);
		int width = Integer.parseInt(opValues[0][0]);
		int height = Integer.parseInt(opValues[0][1]);
		Robot obj = new Robot(width, height);
		List<Object> ans = new ArrayList<>(operators.length);
		ans.add(null);
		for (int i = 1; i < operators.length; i++) {
			if (operators[i].compareTo("step") == 0) {
				int num = Integer.parseInt(opValues[i][0]);
				obj.step(num);
				ans.add(null);
				continue;
			}
			if (operators[i].compareTo("getPos") == 0) {
				
				ans.add(obj.getPos());
				continue;
			}
			if (operators[i].compareTo("getDir") == 0) {
				
				ans.add(obj.getDir());
				continue;
			}
			ans.add(null);
		}
        return JSON.toJSON(ans);
    }
}
