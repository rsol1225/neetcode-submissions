class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        #algorithm
        #loop through the array
            #if the stack is empty append to the stack, like add to it
            #not empty, peek at the top element and see if the current element's temp is greater
                #if it is, subtract the indexes
                #and keep going
        stack = []
        result = [0] * len(temperatures)

        for i,temp in enumerate(temperatures):

            while stack and temperatures[stack[-1]] < temp:
                index = stack.pop()
                result[index] = i-index
            stack.append(i)
        
        return result


