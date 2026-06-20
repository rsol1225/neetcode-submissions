class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        #Input: array of piles
            #piles[i] is the number of bananas in the ith pile
            #h -> number of hours you have to eat all the bananas
        
        #k -> bananas per hour eating rate of k
        # each hour, you may choose a pile of banas and eat k banans from that pile

        #return k such that u can eat all bananas within h hours
        left = 1
        right = max(piles) #O(n)

        res = max(piles)

        while left <= right:
            k = (left+right)//2
            hours = 0

            for p in piles:
                hours += math.ceil(p/k)
            if hours <= h:
                    res = min(res,k)
                    right = k-1
            else:
                    left = k + 1
        
        return res



