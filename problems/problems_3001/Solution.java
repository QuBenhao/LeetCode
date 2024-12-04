package problems.problems_3001;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int minMovesToCaptureTheQueen(int a, int b, int c, int d, int e, int f) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int a = Integer.parseInt(inputJsonValues[0]);
		int b = Integer.parseInt(inputJsonValues[1]);
		int c = Integer.parseInt(inputJsonValues[2]);
		int d = Integer.parseInt(inputJsonValues[3]);
		int e = Integer.parseInt(inputJsonValues[4]);
		int f = Integer.parseInt(inputJsonValues[5]);
        return JSON.toJSON(minMovesToCaptureTheQueen(a, b, c, d, e, f));
    }
}
