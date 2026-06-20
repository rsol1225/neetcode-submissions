class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        #Understand:
        #1. Is the array sorted? It doesn't matter (if using hashmap)
        #2. There's always an answer
        #3. nums = [6,7,8] k= 2
            #which elements would I return
        
        #Match:
        #Hashmaps --> store the frequency of each element
        #Maxheaps --> O(nlogn)
        #Bucket sort
            #[1,2,2,3,3,3] k = 2
                #hashmap stored the frequencies of each number
                #{3:3, 1:1, 2:2}. ---> unordered
                #bucket sort = [[],[],[],[]]
                    #frequencies 0,1,2,3,4,5,...nums.length
                        #In bucket sort array: each frequency corresponds with elements that have those frequencies
                        # in the nums array
                
                #result array
                #loop backwards on the bucket sort array for i in range...
                        # if list in the bucket sort array lenght is > 0:
                            #result.append()
                        # if length of the result array == k:
                            #return the result 

        hashMap = {}

        #includes 0
        freq = [[] for i in range (len(nums)+1)]

        #Store the frequencies of each number
        for i in nums:
            hashMap[i] = 1 + hashMap.get(i,0)
        
        #Loop through the hashMap and ensure the freq correspond with the correct index
        #[2,2,2,3,3,3,1,1] 
        #{2:3, 3:3, 1:2}

        for num, occurence in hashMap.items():
            freq[occurence].append(num)
        
        result = []
        #frequency array 0:[] 1:[] 2:[1] 3:[2,3] 4:[]....8:[]

        #range(start, step, stop) and stops before
        for j in range(len(freq)-1, -1, -1): #O(n)
            for n in freq[j]:  #would visit each element max once                #O()
                result.append(n)
            if len(result) == k:
                return result
        return

        
        #Evaluate time complexity
        # HashMap frequences : O(n)
        # Developing the frequency array: + O(n) #need to loop through the frequences max n
        # O(n)

        #Time complexity = O(n)

            