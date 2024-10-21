from collections import defaultdict
 def mergeAlternately(self, word1: str, word2: str) -> str:
    for i in range(0, len(word1), 2):
        print(word1[i])



# Test cases
word1 = "abc", word2 = "pqr"
# Run the function and print the results
print(mergeAlternately(word1 ,word2))
