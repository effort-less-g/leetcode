class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        
        potions.sort()
        ans = []
        flag = True

        for spell in spells:
            
            mid = 0
            left = 0 
            right = len(potions) - 1
            flag = True

            while left <= right:
                mid = left + (right - left) // 2

                s1 = spell * potions[mid]
                if mid-1 < 0:
                    s2 = 0
                else:
                    s2 = spell * potions[mid - 1]

                if s1 >= success and s2 >= success:
                    right = mid - 1
                
                elif s1 < success and s2 < success:
                    left = mid + 1
                
                else:
                    break
            
            # print(mid, left, right)

            if left > right:
                ans.append(0)
            else:
                ans.append(len(potions) - mid)
        
        return ans

                    
