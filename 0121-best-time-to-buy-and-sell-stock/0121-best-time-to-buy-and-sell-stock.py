class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #optimal solution
        m=prices[0]
        profit=0
        l=len(prices)
        for i in range(1,l):
            cost=prices[i]-m
            profit=max(profit,cost)
            m=min(m,prices[i])
        return profit




        # #brute force
        # l=len(prices)
        # sell=0
        # for i in range(l):
        #     for j in range(i+1,l):
        #         tmp=prices[j]-prices[i]
        #         sell=max(sell,tmp)
        # return sell
                