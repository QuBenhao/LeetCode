package problems.problems_2296;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


class TextEditor {

    public TextEditor() {
        
    }
    
    public void addText(String text) {
        
    }
    
    public int deleteText(int k) {
        
    }
    
    public String cursorLeft(int k) {
        
    }
    
    public String cursorRight(int k) {
        
    }
}

/**
 * Your TextEditor object will be instantiated and called as such:
 * TextEditor obj = new TextEditor();
 * obj.addText(text);
 * int param_2 = obj.deleteText(k);
 * String param_3 = obj.cursorLeft(k);
 * String param_4 = obj.cursorRight(k);
 */

public class Solution extends BaseSolution {


    @Override
    public Object solve(String[] inputJsonValues) {
        String[] operators = jsonArrayToStringArray(inputJsonValues[0]);
		String[][] opValues = jsonArrayToString2DArray(inputJsonValues[1]);
		
		TextEditor obj = new TextEditor();
		List<Object> ans = new ArrayList<>(operators.length);
		ans.add(null);
		for (int i = 1; i < operators.length; i++) {
			if (operators[i].compareTo("addText") == 0) {
				String text = jsonStringToString(opValues[i][0]);
				obj.addText(text);
				ans.add(null);
				continue;
			}
			if (operators[i].compareTo("deleteText") == 0) {
				int k = Integer.parseInt(opValues[i][0]);
				ans.add(obj.deleteText(k));
				continue;
			}
			if (operators[i].compareTo("cursorLeft") == 0) {
				int k = Integer.parseInt(opValues[i][0]);
				ans.add(obj.cursorLeft(k));
				continue;
			}
			if (operators[i].compareTo("cursorRight") == 0) {
				int k = Integer.parseInt(opValues[i][0]);
				ans.add(obj.cursorRight(k));
				continue;
			}
			ans.add(null);
		}
        return JSON.toJSON(ans);
    }
}
