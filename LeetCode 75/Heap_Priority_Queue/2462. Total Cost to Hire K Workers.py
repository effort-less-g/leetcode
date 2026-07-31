class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        candidates1 = []
        candidates2 = []

        size = len(costs)
        i, j = 0, size - 1
        sum1 = 0
        count1 = 0
        flag = False

        while count1 < k:

            print(i, j)

            while len(candidates1) < candidates:

                if i < j:
                    heappush(candidates1, costs[i])
                    i += 1    

                elif i == j:
                    heappush(candidates1, costs[i])
                    i += 1
                    flag = True
                else:
                    break

            while len(candidates2) < candidates:

                if i < j:
                    heappush(candidates2, costs[j])
                    j -= 1    
                elif i == j and not flag:
                    heappush(candidates2, costs[j])
                    j -= 1
                else:
                    break

            print(candidates1, candidates2)
            
            tmp = 0

            if not candidates1 and not candidates2:
                break
            elif not candidates1:
                tmp = heappop(candidates2)
            elif not candidates2:
                tmp = heappop(candidates1)

            elif candidates1[0] == candidates2[0] and i < j:
                if costs[i] < costs[j]:
                    tmp = heappop(candidates1)
                else:
                    tmp = heappop(candidates2)
            
            elif candidates1[0] < candidates2[0]:
                tmp = heappop(candidates1)
            else:
                tmp = heappop(candidates2)

            print(tmp)
            sum1 += tmp

            count1 += 1

        candidates1 = []
        candidates2 = []

        size = len(costs)
        i, j = 0, size - 1
        sum2 = 0
        count2 = 0
        flag = False

        while count2 < k:

            print(i, j)

            while len(candidates1) < candidates:

                if i < j:
                    heappush(candidates1, costs[i])
                    i += 1    

                elif i == j:
                    heappush(candidates1, costs[i])
                    i += 1
                    flag = True
                else:
                    break

            while len(candidates2) < candidates:

                if i < j:
                    heappush(candidates2, costs[j])
                    j -= 1    
                elif i == j and not flag:
                    heappush(candidates2, costs[j])
                    j -= 1
                else:
                    break

            print(candidates1, candidates2)
            
            tmp = 0

            if not candidates1 and not candidates2:
                break
            elif not candidates1:
                tmp = heappop(candidates2)
            elif not candidates2:
                tmp = heappop(candidates1)

            elif candidates1[0] == candidates2[0] and i < j:
                if costs[j] < costs[i]:
                    tmp = heappop(candidates2)
                else:
                    tmp = heappop(candidates1)
            
            elif candidates2[0] < candidates1[0]:
                tmp = heappop(candidates2)
            else:
                tmp = heappop(candidates1)

            print(tmp)
            sum2 += tmp

            count2 += 1

        return min(sum1, sum2)
