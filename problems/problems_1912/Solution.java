package problems.problems_1912;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


class MovieRentingSystem {

    public MovieRentingSystem(int n, int[][] entries) {
        
    }
    
    public List<Integer> search(int movie) {
        
    }
    
    public void rent(int shop, int movie) {
        
    }
    
    public void drop(int shop, int movie) {
        
    }
    
    public List<List<Integer>> report() {
        
    }
}

/**
 * Your MovieRentingSystem object will be instantiated and called as such:
 * MovieRentingSystem obj = new MovieRentingSystem(n, entries);
 * List<Integer> param_1 = obj.search(movie);
 * obj.rent(shop,movie);
 * obj.drop(shop,movie);
 * List<List<Integer>> param_4 = obj.report();
 */

public class Solution extends BaseSolution {


    @Override
    public Object solve(String[] inputJsonValues) {
        String[] operators = jsonArrayToStringArray(inputJsonValues[0]);
		String[][] opValues = jsonArrayToString2DArray(inputJsonValues[1]);
		int n = Integer.parseInt(opValues[0][0]);
		int[][] entries = jsonArrayToInt2DArray(opValues[0][1]);
		MovieRentingSystem obj = new MovieRentingSystem(n, entries);
		List<Object> ans = new ArrayList<>(operators.length);
		ans.add(null);
		for (int i = 1; i < operators.length; i++) {
			if (operators[i].compareTo("search") == 0) {
				int movie = Integer.parseInt(opValues[i][0]);
				ans.add(obj.search(movie));
				continue;
			}
			if (operators[i].compareTo("rent") == 0) {
				int shop = Integer.parseInt(opValues[i][0]);
				int movie = Integer.parseInt(opValues[i][1]);
				obj.rent(shop, movie);
				ans.add(null);
				continue;
			}
			if (operators[i].compareTo("drop") == 0) {
				int shop = Integer.parseInt(opValues[i][0]);
				int movie = Integer.parseInt(opValues[i][1]);
				obj.drop(shop, movie);
				ans.add(null);
				continue;
			}
			if (operators[i].compareTo("report") == 0) {
				
				ans.add(obj.report());
				continue;
			}
			ans.add(null);
		}
        return JSON.toJSON(ans);
    }
}
