package problems.problems_2241;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


class ATM {

    public ATM() {
        
    }
    
    public void deposit(int[] banknotesCount) {
        
    }
    
    public int[] withdraw(int amount) {
        
    }
}

/**
 * Your ATM object will be instantiated and called as such:
 * ATM obj = new ATM();
 * obj.deposit(banknotesCount);
 * int[] param_2 = obj.withdraw(amount);
 */

public class Solution extends BaseSolution {


    @Override
    public Object solve(String[] inputJsonValues) {
        String[] operators = jsonArrayToStringArray(inputJsonValues[0]);
		String[][] opValues = jsonArrayToString2DArray(inputJsonValues[1]);
		
		ATM obj = new ATM();
		List<Object> ans = new ArrayList<>(operators.length);
		ans.add(null);
		for (int i = 1; i < operators.length; i++) {
			if (operators[i].compareTo("deposit") == 0) {
				int[] banknotesCount = jsonArrayToIntArray(opValues[i][0]);
				obj.deposit(banknotesCount);
				ans.add(null);
				continue;
			}
			if (operators[i].compareTo("withdraw") == 0) {
				int amount = Integer.parseInt(opValues[i][0]);
				ans.add(obj.withdraw(amount));
				continue;
			}
			ans.add(null);
		}
        return JSON.toJSON(ans);
    }
}
