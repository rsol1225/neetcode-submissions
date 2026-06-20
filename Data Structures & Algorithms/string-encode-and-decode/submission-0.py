class Solution:

    #Input: ["Hello", "World"]
    #Output: "5#hello5#world"

    #Input: ["Hello", "World"]
    # "#" embedded between each string
    #Output: "Hello#World"

    #Input: ["He#llo", "World"]
    #Output: "He#llo#World"

    def encode(self, strs: List[str]) -> str:
        #result 
        #encoded_symbol ="#"
        #loop s through the strings
            #get the length of the string
            #get the string itself
            #result += str(len(s)) + encoded_symbol + s
        #return result

        result = ""
        encoded_symbol ="#"
        for s in strs:
            result += str(len(s)) + encoded_symbol + s
        return result

    #Input: "6#He#llo5#World"
    #Output: ["He#llo", "World"]

    #loop through the string
        #Number and Pound symbol
        #grab the first 2 numbers
        #substring to grab the 6 characters after the pound

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        #Walk through the array
        while i < len(s):
            j = i
            #Walk through the string, to see where the string begins
            while s[j] != "#":
                j += 1
            #Get the string knowing how many characters long it is
            length_of_word = s[i:j]

            #Skipping over the pound
            i = j + 1
            word = s[i:i+int(length_of_word)]
            result.append(word)

            i += int(length_of_word)

        return result

