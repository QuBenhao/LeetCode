package problems.problems_1401;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public boolean checkOverlap(int radius, int xCenter, int yCenter, int x1, int y1, int x2, int y2) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int radius = Integer.parseInt(inputJsonValues[0]);
		int xCenter = Integer.parseInt(inputJsonValues[1]);
		int yCenter = Integer.parseInt(inputJsonValues[2]);
		int x1 = Integer.parseInt(inputJsonValues[3]);
		int y1 = Integer.parseInt(inputJsonValues[4]);
		int x2 = Integer.parseInt(inputJsonValues[5]);
		int y2 = Integer.parseInt(inputJsonValues[6]);
        return JSON.toJSON(checkOverlap(radius, xCenter, yCenter, x1, y1, x2, y2));
    }
}
