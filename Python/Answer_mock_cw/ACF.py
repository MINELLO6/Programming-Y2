"""
    Write a program that finds the greatest common power of 3 which divides two integers.

    Note: the function should return 3 to that power, for example the greatest common power of 3 in 6 and 24 is 3.

    Recall that any integer divides 0 and therefore the greatest common divisor of 0 and 0, gcd(0,0) is "infinity",

    which in Python is defined by using "math.inf".
"""

# import math
#
#
# def common_power_of_three(a, b):
#     if a == 0 and b == 0:
#         return math.inf
#     else:
#         n = 0
#         control = True
#         while 1:
#             a, r1 = divmod(a, 3)
#             b, r2 = divmod(b, 3)
#             control = (r1 or r2)
#             if control == False:
#                 n += 1
#             else:
#                 break
#         return 3 ** n


"""
    Write another function that improves on the function from (a) so that it computes the greatest common power of 3 
    which divides all elements in a given list. 

    Note: just as in part (a) the function should return 3 to that power.  
"""

# import math
#
#
# def common_power_of_three_list(alist):
#     set_tep = set(alist)
#     alist = list(set_tep)
#     if set(alist) == {0}:
#         return math.inf
#     else:
#         r = []
#         n = 0
#         while 1:
#             for element in range(len(alist)):
#                 alist[element], rm = divmod(alist[element], 3)
#                 r.append(rm)
#             if set(r) == {0}:
#                 n += 1
#             else:
#                 break
#     return 3 ** n


"""
    Write yet another another function that improves on the previous one so that 
    it computes the greatest common power of a given integer n which divides all elements in a given list.

    Note:  Just as for parts (a) and (b) the function should return n to that power.
"""

# import math
#
#
# def common_power_of_n_list(alist, n):
#     set_tep = set(alist)
#     alist = list(set_tep)
#     if set(alist) == {0}:
#         return math.inf
#     if n == 1:
#         return 1
#     else:
#         # alist.remove(0)
#         r = []
#         num = 0
#         while 1:
#             for i in range(len(alist)):
#                 alist[i], rm = divmod(alist[i], n)
#                 r.append(rm)
#             if set(r) == {0}:
#                 num += 1
#             else:
#                 break
#     return n ** num
