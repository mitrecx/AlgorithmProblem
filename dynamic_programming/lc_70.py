# https://leetcode.cn/problems/climbing-stairs/description/

class Solution:
    def climbStairs(self, n: int) -> int:
        """
        70. 爬楼梯
        假设第 n 阶楼梯有 f(n) 中爬法, 那么有:
        f(n) = f(n-1) + f(n-2)
        即, 从 n-1 阶 跳 1 个台阶到达, 或者 从 n-2 阶 跳 2 个台阶到达
        :param n:
        :return:
        """
        if n == 1:
            return 1
        if n == 2:
            return 2

        f = [1] * n
        f[1] = 2
        for i in range(2, n):
            f[i] = f[i - 1] + f[i - 2]

        return f[n - 1]


if __name__ == '__main__':
    s = Solution()
    print(s.climbStairs(2))
    print(s.climbStairs(3))
    print(s.climbStairs(4))
