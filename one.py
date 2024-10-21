

# def findClosestNumberToZero(numbers):
#     newarr=numbers
#     print(newarr)
#     newarr = sorted( [abs(num) for num in numbers])
#
#     if (-newarr[0] and newarr[0]) in numbers:
#         return -newarr[0]
#     elif (-newarr[0] and not  newarr[0] )in numbers:
#         return -newarr[0]
#     elif (newarr[0] and not -newarr[0]) in numbers:
#         return newarr[0]
#     else:
#         return newarr[0]

    # if -newarr[0] in numbers and newarr[0] in numbers:
    #     return -newarr[0]
    # elif -newarr[0] in numbers and newarr[0] not in numbers:
    #     return -newarr[0]
    # elif newarr[0] in numbers and -newarr[0] not in numbers:
    #     return newarr[0]
    # else:
    #     return newarr[0]


    # if -newarr[0] in numbers:
    #     return -newarr[0]
    # elif newarr[0] in numbers:
    #     return newarr[0]
    # else:
    #     return newarr[0]

#return -newarr[0] if newarr[0] and -newarr[0] in numbers else newarr[0]


#
# def findClosestNumberToZero(numbers):
#     newarr = numbers
#     print(newarr)
#
#     if -newarr[0] in numbers and newarr[0] in numbers:
#         return -newarr[0]
#     elif -newarr[0] in numbers and newarr[0] not in numbers:
#         return -newarr[0]
#     elif newarr[0] in numbers and -newarr[0] not in numbers:
#         return newarr[0]
#     else:
#         return newarr[0]
#
# def findClosestNumberToZero(nums):
#     closest = nums[0]
#     for x in nums:
#         if abs(x) < abs(closest):
#                 closest = x  # the closest = x which gonna be with the - and + sign
#                 # but here I'm checking for the abs value not the positive and negative
#                 # such that 1 and -1 both the same
#                 # SO WE now check for if the + and - both in the list
#     if closest < 0 and abs(closest) in nums:
#             return( -closest)
#     else:
#             return closest
#
#
#
# # Test cases
# test1 = [3, -2, 2, -1, 1, 0]
# test2 = [-4, -2, -3, -1]
# test3 = [5, 2, 3, 1]
# test4 = [0, 0, 0]
# test5 = [1, -1]  #
#
# # Run the function and print the results
# print(findClosestNumberToZero(test1))  # Output: 0
# print(findClosestNumberToZero(test2))  # Output: -1
# print(findClosestNumberToZero(test3))  # Output: 1
# print(findClosestNumberToZero(test4))  # Output: 0
# print(findClosestNumberToZero(test5))  # Output: -1
#
# # #





def findClosestNumberToZero(nums):
    closest = None
    for x in nums:
        if (closest is None) or( abs(x) < abs(closest) )or (abs(x) == abs(closest) and x < closest):
      #             true
      #             false                      true  assing
            closest = x
    return closest


# Order of Execution
# The conditions are evaluated left to right, following the rules of Python's or operator:
#
# First, it checks closest is None.
#
# If True, it skips  the other conditions and updates closest to the current value x.
# If closest is not None, it moves on to abs(x) < abs(closest).
#
# If True, it skips the remaining conditions and updates closest to x.
# If closest is not None and abs(x) >= abs(closest), it finally checks (abs(x) == abs(closest) and x > closest).
#
# If True, it updates closest to the current value of x.
# If none of the conditions are True, the value of closest remains unchanged, and the loop moves to the next number.
#


# Test cases
test1 = [3, -2, 2, -1, 1, 0]
test2 = [-4, -2, -3, -1]
test3 = [5, 2, 3, 1]
test4 = [0, 0, 0]
test5 = [1, -1]

# Run the function and print the results
print(findClosestNumberToZero(test1))  # Output: 0
print(findClosestNumberToZero(test2))  # Output: -1
print(findClosestNumberToZero(test3))  # Output: 1
print(findClosestNumberToZero(test4))  # Output: 0
print(findClosestNumberToZero(test5))  # Output: -1