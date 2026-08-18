class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return max(nums) 
        
        if len(nums) == 3:
            return max(nums[1], nums[0]+nums[2])

        ans = [nums[0], nums[1], nums[0]+nums[2], max(nums[0], nums[1])+nums[3]]
        maxx = max(ans)

        for i in range(4, len(nums)):
            tmp = nums[i] + max(ans[i-2], ans[i-3])
            if maxx < tmp:
                maxx = tmp
            ans.append(tmp)

        # print(ans)

        return maxx
