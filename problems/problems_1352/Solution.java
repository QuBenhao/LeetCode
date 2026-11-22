package problems.problems_1352;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


class ProductOfNumbers {

    public ProductOfNumbers() {
        
    }
    
    public void add(int num) {
        
    }
    
    public int getProduct(int k) {
        
    }
}

/**
 * Your ProductOfNumbers object will be instantiated and called as such:
 * ProductOfNumbers obj = new ProductOfNumbers();
 * obj.add(num);
 * int param_2 = obj.getProduct(k);
 */

public class Solution extends BaseSolution {


    @Override
    public Object solve(String[] inputJsonValues) {
        String[] operators = jsonArrayToStringArray(inputJsonValues[0]);
		String[][] opValues = jsonArrayToString2DArray(inputJsonValues[1]);
		
		ProductOfNumbers obj = new ProductOfNumbers();
		List<Object> ans = new ArrayList<>(operators.length);
		ans.add(null);
		for (int i = 1; i < operators.length; i++) {
			if (operators[i].compareTo("add") == 0) {
				int num = Integer.parseInt(opValues[i][0]);
				obj.add(num);
				ans.add(null);
				continue;
			}
			if (operators[i].compareTo("getProduct") == 0) {
				int k = Integer.parseInt(opValues[i][0]);
				ans.add(obj.getProduct(k));
				continue;
			}
			ans.add(null);
		}
        return JSON.toJSON(ans);
    }
}
