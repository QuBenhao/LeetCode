package problems.problems_3408;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


class TaskManager {

    public TaskManager(List<List<Integer>> tasks) {
        
    }
    
    public void add(int userId, int taskId, int priority) {
        
    }
    
    public void edit(int taskId, int newPriority) {
        
    }
    
    public void rmv(int taskId) {
        
    }
    
    public int execTop() {
        
    }
}

/**
 * Your TaskManager object will be instantiated and called as such:
 * TaskManager obj = new TaskManager(tasks);
 * obj.add(userId,taskId,priority);
 * obj.edit(taskId,newPriority);
 * obj.rmv(taskId);
 * int param_4 = obj.execTop();
 */

public class Solution extends BaseSolution {


    @Override
    public Object solve(String[] inputJsonValues) {
        String[] operators = jsonArrayToStringArray(inputJsonValues[0]);
		String[][] opValues = jsonArrayToString2DArray(inputJsonValues[1]);
		List<List<Integer>> tasks = jsonArrayTo2DIntList(opValues[0][0]);
		TaskManager obj = new TaskManager(tasks);
		List<Object> ans = new ArrayList<>(operators.length);
		ans.add(null);
		for (int i = 1; i < operators.length; i++) {
			if (operators[i].compareTo("add") == 0) {
				int userId = Integer.parseInt(opValues[i][0]);
				int taskId = Integer.parseInt(opValues[i][1]);
				int priority = Integer.parseInt(opValues[i][2]);
				obj.add(userId, taskId, priority);
				ans.add(null);
				continue;
			}
			if (operators[i].compareTo("edit") == 0) {
				int taskId = Integer.parseInt(opValues[i][0]);
				int newPriority = Integer.parseInt(opValues[i][1]);
				obj.edit(taskId, newPriority);
				ans.add(null);
				continue;
			}
			if (operators[i].compareTo("rmv") == 0) {
				int taskId = Integer.parseInt(opValues[i][0]);
				obj.rmv(taskId);
				ans.add(null);
				continue;
			}
			if (operators[i].compareTo("execTop") == 0) {
				
				ans.add(obj.execTop());
				continue;
			}
			ans.add(null);
		}
        return JSON.toJSON(ans);
    }
}
