from collections import defaultdict


def groupAnagrams(strs):


# Test cases
test1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
test2 = [""]
test3 = ["a"]

# Run the function and print the results
print(groupAnagrams(test1))  # Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
print(groupAnagrams(test2))  # Output: [[""]]
print(groupAnagrams(test3))  # Output: [["a"]]
