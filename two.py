from collections import defaultdict


def groupAnagrams(strs):
    # Create a dictionary to hold our groups
    anagram_dict = defaultdict(list)

    # Iterate over each word in the input list
    for word in strs:
        # Sort the word to get the key
        sorted_word = ''.join(sorted(word))
        # Add the word to the corresponding anagram group
        anagram_dict[sorted_word].append(word)

    # Return the values (i.e., the grouped anagrams) as a list
    return list(anagram_dict.values())


# Test cases
test1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
test2 = [""]
test3 = ["a"]

# Run the function and print the results
print(groupAnagrams(test1))  # Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
print(groupAnagrams(test2))  # Output: [[""]]
print(groupAnagrams(test3))  # Output: [["a"]]
