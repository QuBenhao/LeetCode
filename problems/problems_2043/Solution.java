package problems.problems_2043;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


class Bank {

    public Bank(long[] balance) {
        
    }
    
    public boolean transfer(int account1, int account2, long money) {
        
    }
    
    public boolean deposit(int account, long money) {
        
    }
    
    public boolean withdraw(int account, long money) {
        
    }
}

/**
 * Your Bank object will be instantiated and called as such:
 * Bank obj = new Bank(balance);
 * boolean param_1 = obj.transfer(account1,account2,money);
 * boolean param_2 = obj.deposit(account,money);
 * boolean param_3 = obj.withdraw(account,money);
 */

public class Solution extends BaseSolution {


    @Override
    public Object solve(String[] inputJsonValues) {
        String[] operators = jsonArrayToStringArray(inputJsonValues[0]);
		String[][] opValues = jsonArrayToString2DArray(inputJsonValues[1]);
		long[] balance = jsonArrayToLongArray(opValues[0][0]);
		Bank obj = new Bank(balance);
		List<Object> ans = new ArrayList<>(operators.length);
		ans.add(null);
		for (int i = 1; i < operators.length; i++) {
			if (operators[i].compareTo("transfer") == 0) {
				int account1 = Integer.parseInt(opValues[i][0]);
				int account2 = Integer.parseInt(opValues[i][1]);
				long money = Long.parseLong(opValues[i][2]);
				ans.add(obj.transfer(account1, account2, money));
				continue;
			}
			if (operators[i].compareTo("deposit") == 0) {
				int account = Integer.parseInt(opValues[i][0]);
				long money = Long.parseLong(opValues[i][1]);
				ans.add(obj.deposit(account, money));
				continue;
			}
			if (operators[i].compareTo("withdraw") == 0) {
				int account = Integer.parseInt(opValues[i][0]);
				long money = Long.parseLong(opValues[i][1]);
				ans.add(obj.withdraw(account, money));
				continue;
			}
			ans.add(null);
		}
        return JSON.toJSON(ans);
    }
}
