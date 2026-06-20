class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        #[1,2,4,6]
        #prefix elements
        #postfix elements

        #prefix: [1,1,2,4]
            #count that keeps track of the product for the pre
        #postfix: [48,24,6,1]
            #count that keeps track of the product for the post

        #[1,2,3,4]
        #final array [24,12,8,6]
        results = [1] * len(nums)

        postfix_product = 1
        for i in range(len(nums)-1,-1,-1):
            results[i] = postfix_product
            postfix_product *= nums[i]
        
        prefix_product = 1;
        for i in range(0, len(nums)):
            results[i] *= prefix_product
            prefix_product *= nums[i]
        
       
        
        return results

