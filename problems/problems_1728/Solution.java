package problems.problems_1728;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public boolean canMouseWin(String[] grid, int catJump, int mouseJump) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String[] grid = jsonArrayToStringArray(inputJsonValues[0]);
		int catJump = Integer.parseInt(inputJsonValues[1]);
		int mouseJump = Integer.parseInt(inputJsonValues[2]);
        return JSON.toJSON(canMouseWin(grid, catJump, mouseJump));
    }
}
