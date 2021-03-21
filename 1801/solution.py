import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.getNumberOfBacklogOrders([x[:] for x in test_input])

    def getNumberOfBacklogOrders(self, orders):
        """
        :type orders: List[List[int]]
        :rtype: int
        """
        import heapq
        buys, sells = [], []
        for p,a,t in orders:
            if t == 0:
                while sells:
                    p_, a_ = heapq.heappop(sells)
                    if p_ <= p:
                        if a >= a_:
                            a -= a_
                        else:
                            heapq.heappush(sells, (p_, a_-a))
                            a = 0
                            break
                    else:
                        heapq.heappush(sells, (p_, a_))
                        break
                if a:
                    heapq.heappush(buys, (-p, a))
            else:
                while buys:
                    p_, a_ = heapq.heappop(buys)
                    p_ = -p_
                    if p_ >= p:
                        if a >= a_:
                            a -= a_
                        else:
                            heapq.heappush(buys, (-p_, a_-a))
                            a = 0
                            break
                    else:
                        heapq.heappush(buys, (-p_, a_))
                        break
                if a:
                    heapq.heappush(sells, (p, a))
        return (sum(x[1] for x in sells) + sum(x[1] for x in buys)) % (10**9+7)
