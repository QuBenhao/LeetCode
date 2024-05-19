import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.find132pattern(list(test_input))

    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        """
        We have a six options for solving this problem 132
        1. Get 1 3 then 2
        2. Get 1 2 then 3
        3. Get 3 2 then 1
        4. Get 3 1 then 2
        5. Get 2 3 then 1
        6. Get 2 1 then 3
        
        What is a easiest way for this problem.
        First, finding 1, 3 then 2 is difficult. 
        because we checked double for finding 2. upper and lower. 
        However, Get 1, 2 then 3 is easy. we check only one for finding 3. we do not have to check 3 with 1.
        So Method 2, 3, 5, 6 is good.
        
        And I want to check numbers only one direction.
        If I select 1, 2 then 3, I need to select 1 from left direction and select 2 from right direction.
        It is difficult.
        
        If I select numbers from left, That is Method 1. If I select numbers from right, that is Method 5.
        
        So Method 5 is easiest way for this problem.
        Left Problem is how to write the code for method 5.
        
        The 3 is always the maximum from right. It is clear.
        The 2 is a maximum number which in 3's left. => This part is O(N)
        But If we use stack, we can optimize this part to O(1)
        """
        last, stack = float("-inf"), []
        for num in reversed(nums):
            if num < last:
                return True
            while stack and stack[-1] < num:
                last = stack.pop()
            stack.append(num)
        return False
