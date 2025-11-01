class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if not prices:
            return 0
        
        min_price = prices[0]
        max_profit = 0
        
        for price in prices[1:]:
            # 更新最低买入价
            if price < min_price:
                min_price = price
            # 计算当天卖出的利润
            profit = price - min_price
            # 更新最大利润
            if profit > max_profit:
                max_profit = profit
        
        return max_profit