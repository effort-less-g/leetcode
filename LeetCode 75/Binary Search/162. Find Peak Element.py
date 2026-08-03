class Solution:

    def rec(self, nums, left, right):

        # print(left, right)

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid-1] < nums[mid] > nums[mid + 1]:
                return mid
            else:
                ans = self.rec(nums, mid+1, right)
                if ans:
                    return ans
                else:
                    return self.rec(nums, left, mid-1)

    def findPeakElement(self, nums: List[int]) -> int:
        left = 0 
        right = len(nums) - 1

        if len(nums) == 1:
            return 0
        elif nums[0] > nums[1]:
            return 0
        elif nums[-1] > nums[-2]:
            return len(nums) - 1
        else:
            res = self.rec(nums, left, right)

            if res:
                return res
            else:
                return nums.index(max(nums))
