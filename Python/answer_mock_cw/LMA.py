"""
    INTRODUCTION
    It is possible to represent polynomials as vectors (which we in turn can represent as lists in Python) so that, for instance, the polynomial

    20 i + 30 + (73 i - 42)z - (24 i + 57) z^{2} - (15 i - 2) z^{3} + z^{4}

    is represented by the list

    [20i+30,73 i - 42,-(24 i + 57),-(15 i - 2),1].

    More generally a polynomial of degree n (with terms written in increasing degree):

    p = a_0 + a_1 z + a_2 z^2 +\cdots + a_n z^{n}

    is represented by the list of coefficients:

    \mathbf{c}_p = [a_0,a_1,a_2,\ldots,a_n].
"""

"""
    Write a function `evaluate_polynomial` that has two arguments `alist` and `z0`, where `alist` is a list of coefficients corresponding to a polynomial (as explained above) and z_0 is a real or complex number. 
    
    The function should return the value of the polynomial evaluated at the point `z=z0`.
"""


# def evaluate_polynomial(alist, z0):
#     sum = 0
#     for i in range(len(alist)):
#         sum += alist[i] * (z0 ** i)
#     return sum


"""
    Write a function 'add_polynomials' which takes two arguments: `alist` and `blist`  consisting of coefficients corresponding to two polynomials, p and q. The function should return a list `clist` consisting of coefficients for the polynomial p + q.

    (Hint: note that `alist` and `blist` can be of different length.)   
"""


# def add_polynomials(alist, blist):
#     clist = []
#     for i in range(min(len(alist), len(blist))):
#         clist.append(alist[i] + blist[i])
#     if len(alist) > len(blist):
#         clist.extend(alist[len(blist):])
#     if len(alist) < len(blist):
#         clist.extend(blist[len(alist):])
#     return clist


"""
    Write a program that takes arguments `alist` and `N` where `alist`  is a list of coefficients for a polynomial p and  N is an integer.

    The function should return a set of all zeros of the form a+bi, where a and b are integers with absolute value less than or equal to N, of the corresponding polynomial p.

    Note: In your function you should use the function `evaluate_polynomial` from part (a) to evaluate a polynomial given by a list of coefficients. You can assume that this function is defined and works as intended according to the description in part (a) of this problem (In other words, you DO NOT need to write it here again)
"""


# def find_zeros_within_bound(alist, N):
#     result_set = set({})
#     for i in range(-N, N + 1):
#         for s in range(-N, N + 1):
#             a = i
#             b = s
#             if evaluate_polynomial(alist, complex(a, b)) == 0:
#                 result_set.add(complex(a, b))
#     return result_set
