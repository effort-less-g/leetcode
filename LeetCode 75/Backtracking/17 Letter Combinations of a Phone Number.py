class Solution:

    combos = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }

    ans = []
    digits = ""

    def bt_dfs(self, path, digit, length):
        print(digit)

        if len(path) == length:
            return path

        for choice in self.combos[digit]:
            path += choice
            ind = len(path)
            if len(path) == length:
                ind -= 1
            res = self.bt_dfs(path, self.digits[ind], length)
            if res:
                self.ans.append(res)
            path = path[:-1]

    def letterCombinations(self, digits: str) -> List[str]:

        path = ""
        self.ans = []
        self.digits = digits
        self.bt_dfs(path, digits[0], len(digits))
        return self.ans
