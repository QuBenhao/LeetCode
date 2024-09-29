package problems.problems_2073;

import com.alibaba.fastjson.JSON;

import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int timeRequiredToBuy(int[] tickets, int k) {
        int ans = 0;
        int n = tickets.length;
        int ticketToBuy = tickets[k];
        for (int i = 0; i < n; i++) {
            ans += Math.min(tickets[i], i > k ? ticketToBuy - 1 : ticketToBuy);
        }
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] tickets = jsonArrayToIntArray(inputJsonValues[0]);
		int k = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(timeRequiredToBuy(tickets, k));
    }
}
