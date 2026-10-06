import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxLength(list(test_input))

    def maxLength(self, arr):
        """
        :type arr: List[str]
        :rtype: int
        """
        # Preprocess the data by removing strings with duplicate characters
        arr = [t for s in arr if len(t := set(s)) == len(s)]
        # Estimate an upper bound on the result
        predict = len(set().union(*arr))
        n = len(arr)
        self.curr = set()
        self.ans = 0

        def dfs(idx):
            # Update the answer with the current selection's length
            self.ans = max(self.ans, len(self.curr))
            # Stop searching if the maximum possible result is reached, or if the current selection plus the remaining upper bound cannot improve the answer
            if self.ans == predict or idx == n or len(self.curr) + len(set().union(*arr[idx:])) < self.ans:
                return
            # Backtrack from idx to n to maximize the current 0/1 knapsack selection combined with the remaining items
            for i in range(idx, n):
                # The current selection does not overlap with arr[idx]
                if not self.curr & arr[i]:
                    # Add to the selection, A+B
                    self.curr |= arr[i]
                    # Evaluate the maximum for the new selection
                    dfs(i + 1)
                    # Backtrack and continue searching for the maximum, (A+B) - B
                    self.curr ^= arr[i]

        dfs(0)
        return self.ans
