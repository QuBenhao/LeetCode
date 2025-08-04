package problems.problems_2069;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


class Robot {
	private static final String[] DIRS = {"East", "North", "West", "South"};
	private final int m, n, total;
	private int loc;
	private boolean moved, cached;
	private int x, y, dir;

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
		cached = false;
    }
    
    public int[] getPos() {
        move();
		return new int[]{x, y};
    }
    
    public String getDir() {
		move();
        return DIRS[dir];
    }

	private void move() {
		if (cached) {
			return;
		}
		cached = true;
		if (!moved) {
			x = 0;
			y = 0;
			dir = 0;
			return;
		}
		if (loc < m) {
			x = loc;
			y = 0;
			dir = loc == 0 ? 3 : 0; // East
			return;
		}
		if (loc < m + n - 1) {
			x = m - 1;
			y = loc - m + 1;
			dir = 1; // North
			return;
		}
		if (loc < 2 * m + n - 2) {
			x = m - 1 - (loc - m - n + 2);
			y = n - 1;
			dir = 2; // West
			return;
		}
		x = 0;
		y = total - loc;
		dir = 3; // South
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
