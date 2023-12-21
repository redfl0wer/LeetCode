class Solution(object):
    def runningSum(self, nums):
        runningSum = []
        sum = 0
        for i in range (len(nums)):
            sum += nums[i]
            runningSum.append(sum)
        return runningSum

        