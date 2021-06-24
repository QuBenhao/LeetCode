import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        inventory, orders = test_input
        return self.maxProfit(list(inventory), orders)

    def maxProfit(self, inventory, orders):
        """
        :type inventory: List[int]
        :type orders: int
        :rtype: int
        """
        val = 0
        inventory.append(0)
        inventory.sort()

        i = len(inventory) - 1
        width = 1

        while i > 0:
            while inventory[i] == inventory[i - 1]:
                i -= 1
                width += 1

            high = inventory[i]
            low = inventory[i - 1]

            if orders < (high - low) * width:
                h = orders // width
                val += self.get_matrix(high, h, width) + (orders - h * width) * (high - h)
                val %= (10 ** 9 + 7)
                break

            val += self.get_matrix(high, high - low, width)
            orders -= (high - low) * width

            width +=1
            i -= 1

            val %= (10**9 + 7)

        return val

    def get_matrix(self, top: int, h: int, w: int):
        return h * (top + (top - h + 1)) * w // 2
