class Solution(object):
    def maximumWealth(self, accounts):
        rowSum = []
        for row in accounts:
            rowSum.append(sum(row))
        return max(rowSum)                    
        