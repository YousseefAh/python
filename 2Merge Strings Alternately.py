# class Solution:
#     def mergeAlternately(self, word1: str, word2: str) -> str:
#         A,B=len(word1),len(word2)
#         a,b=0,0
#         word=1
#         arr=[]
#         while a<A and b<B:
#             if word ==1:
#                 arr.append(word1[a])
#                 a+=1
#                 word=2
#             if word==2:
#                 arr.append(word2[b])
#                 b+=1
#                 word=1
#             while a <A:
#                 arr.append(word1[a])
#                 a+=1
#             while b<B:
#                 arr.append(word2[b])
#                 b+=1
#         return ''.join(arr)
#
# #
# # Test cases
# solution = Solution()
# print(solution.mergeAlternately("abc", "pqrm"))  # Output: "apbqcr"
# print(solution.mergeAlternately("ab", "pqrs"))  # Output: "apbqrs"
# print(solution.mergeAlternately("abcd", "pq"))  # Output: "apbqcd"
#




class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        A, B = len(word1), len(word2)
        a, b = 0, 0
        arr = []

        while a < A and b < B:
            arr.append(word1[a])
            a += 1
            arr.append(word2[b])
            b += 1

        arr.extend(word1[a:])
        arr.extend(word2[b:])
        return ''.join(arr)

# Test cases
solution = Solution()
print(solution.mergeAlternately("abc", "pqrm"))  # Output: "apbqcr"
print(solution.mergeAlternately("ab", "pqrs"))   # Output: "apbqrs"
print(solution.mergeAlternately("abcd", "pq"))   # Output: "apbqcd""abcd", "pq"))  # Output: "apbqcd"