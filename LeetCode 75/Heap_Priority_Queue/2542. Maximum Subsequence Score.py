from heapq import heappush, heappop

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        
        heap = []
        
        sorted_tuple = list(zip(nums1, nums2))

        sorted_tuple.sort(key=lambda x:-x[1])

        # print(sorted_tuple)

        res, sum = 0, 0

        for a, b in sorted_tuple:
            sum += a 
            heappush(heap, a)
            # print(heap)
            if len(heap) == k:
                res = max(res, sum*b)
                sum -= heappop(heap)

        return res
