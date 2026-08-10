class Solution:

    ans = []
    res = []
    k = 2
    n = 1
    
    def bt_dfs(self, idx):

        self.ans.append(idx)

        if len(self.ans) > self.k:
            return

        # print(self.ans)

        if sum(self.ans) == self.n and len(self.ans) == self.k:
            # print("JAJFJADJF")
            self.res.append(list.copy(self.ans))
            # print(self.res)
            return

        for i in range(idx+1, 10):
            self.bt_dfs(i)
            self.ans.pop()


    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.res = []
        self.ans = []
        self.k = k
        self.n = n

        for i in range(1, 10):
            self.bt_dfs(i)
            self.ans.pop()

        return self.res
