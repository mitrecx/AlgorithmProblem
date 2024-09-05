# https://leetcode.cn/problems/house-robber/description/
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        198. 打家劫舍
        遍历每一家, 可以选择 偷 或者 不偷.
        设 f(n) 表示到 n 家可以 偷 到的最多金额, 那么:
        f(n) = max(f(n-1), f(n-2) + nums[n])
        即, f(n) 取决于偷不偷前一家.
        :param nums:
        :return:
        """
        if len(nums) == 1:
            return nums[0]

        f = [0] * len(nums)
        f[0] = nums[0]
        f[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            f[i] = max(f[i - 1], f[i - 2] + nums[i])

        return f[len(nums) - 1]


if __name__ == '__main__':
    s = Solution()
    print(s.rob([1, 2, 3, 1]))
