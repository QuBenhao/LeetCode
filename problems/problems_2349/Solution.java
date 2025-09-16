package problems.problems_2349;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


class NumberContainers {

    public NumberContainers() {
        
    }
    
    public void change(int index, int number) {
        
    }
    
    public int find(int number) {
        
    }
}

/**
 * Your NumberContainers object will be instantiated and called as such:
 * NumberContainers obj = new NumberContainers();
 * obj.change(index,number);
 * int param_2 = obj.find(number);
 */

public class Solution extends BaseSolution {


    @Override
    public Object solve(String[] inputJsonValues) {
        String[] operators = jsonArrayToStringArray(inputJsonValues[0]);
		String[][] opValues = jsonArrayToString2DArray(inputJsonValues[1]);
		
		NumberContainers obj = new NumberContainers();
		List<Object> ans = new ArrayList<>(operators.length);
		ans.add(null);
		for (int i = 1; i < operators.length; i++) {
			if (operators[i].compareTo("change") == 0) {
				int index = Integer.parseInt(opValues[i][0]);
				int number = Integer.parseInt(opValues[i][1]);
				obj.change(index, number);
				ans.add(null);
				continue;
			}
			if (operators[i].compareTo("find") == 0) {
				int number = Integer.parseInt(opValues[i][0]);
				ans.add(obj.find(number));
				continue;
			}
			ans.add(null);
		}
        return JSON.toJSON(ans);
    }
}
