package problems.problems_3484;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


class Spreadsheet {

    public Spreadsheet(int rows) {
        
    }
    
    public void setCell(String cell, int value) {
        
    }
    
    public void resetCell(String cell) {
        
    }
    
    public int getValue(String formula) {
        
    }
}

/**
 * Your Spreadsheet object will be instantiated and called as such:
 * Spreadsheet obj = new Spreadsheet(rows);
 * obj.setCell(cell,value);
 * obj.resetCell(cell);
 * int param_3 = obj.getValue(formula);
 */

public class Solution extends BaseSolution {


    @Override
    public Object solve(String[] inputJsonValues) {
        String[] operators = jsonArrayToStringArray(inputJsonValues[0]);
		String[][] opValues = jsonArrayToString2DArray(inputJsonValues[1]);
		int rows = Integer.parseInt(opValues[0][0]);
		Spreadsheet obj = new Spreadsheet(rows);
		List<Object> ans = new ArrayList<>(operators.length);
		ans.add(null);
		for (int i = 1; i < operators.length; i++) {
			if (operators[i].compareTo("setCell") == 0) {
				String cell = jsonStringToString(opValues[i][0]);
				int value = Integer.parseInt(opValues[i][1]);
				obj.setCell(cell, value);
				ans.add(null);
				continue;
			}
			if (operators[i].compareTo("resetCell") == 0) {
				String cell = jsonStringToString(opValues[i][0]);
				obj.resetCell(cell);
				ans.add(null);
				continue;
			}
			if (operators[i].compareTo("getValue") == 0) {
				String formula = jsonStringToString(opValues[i][0]);
				ans.add(obj.getValue(formula));
				continue;
			}
			ans.add(null);
		}
        return JSON.toJSON(ans);
    }
}
