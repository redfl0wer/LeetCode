class Solution(object):
    def numberOfSteps(self, num):
        count = 0
        while num != 0:
            if num % 2 == 0:
                num = num // 2
                count += 1
            if num == 1:
                count += 1
                num = 0
            if num % 2 == 1:
                num = (num - 1) // 2
                count = count + 2
                
        return count    
            
                