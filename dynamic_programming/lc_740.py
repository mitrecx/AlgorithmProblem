# https://leetcode.cn/problems/delete-and-earn/description/
from collections import defaultdict
from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        """"
        1. 如果需要删除数字 x, 那么所有重复的 x 都要删除, 可以获得最多分数.
        2. 不用先排序, 用空间换时间, 用 map 记录 数字 和 分数 关心.
        3. 从 0 到 maxNum(nums 中的最大值) 遍历, 用 dp[] 记录到当前数字能获得的最多分数.
        """
        # map, key: 数字, value: 删除该数字可以获得的总分数
        points = defaultdict(int)
        max_number = 0
        for num in nums:
            max_number = max(num, max_number)
            points[num] += num

        # 记录到当前数字能获得的最多分数
        dp = [0] * (max_number + 1)
        # dp[0]=0, dp[1] = points[1]
        dp[1] = points[1]
        for i in range(2, max_number+1):
            dp[i] = max(dp[i-1], dp[i-2]+points[i])

        return dp[max_number]


if __name__ == '__main__':
    nums = [3, 4, 2]
    solution = Solution()
    # Output: 6
    print(solution.deleteAndEarn(nums))
