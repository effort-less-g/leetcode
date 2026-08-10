class Solution:
    def tribonacci(self, n: int) -> int:

        tribonachi = [0, 1, 1]

        if n < 3:
            return tribonachi[n]

        for i in range(3, n+1):
            a = tribonachi[i-3]
            b = tribonachi[i-2]
            c = tribonachi[i-1]
            tribonachi.append(a+b+c)

        return tribonachi[-1]
