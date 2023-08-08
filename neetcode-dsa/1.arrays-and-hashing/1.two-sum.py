#
# @lc app=leetcode id=1 lang=python
#
# [1] Two Sum
#

# @lc code=start
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        s = sorted(enumerate(nums), key = lambda x: x[1])
        i, j = 0, len(nums) - 1
        sum = s[i][1] + s[j][1]
        while sum != target:
          if sum < target:
            i += 1
          else:
            j -= 1
          sum = s[i][1] + s[j][1]
        lower, upper = s[i][0], s[j][0] 
        return [lower, upper]
# @lc code=end