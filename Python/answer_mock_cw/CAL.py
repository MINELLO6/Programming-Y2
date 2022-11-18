"""
    INTRODUCTION
    For a 'nice' function f defined on a (short) finite interval [a,b] it is possible to approximate the integral over this interval by

    \int_{a}^{b} f(x) dx \approx \frac{1}{2}(b-a)[f(a)+f(b)]-\frac{1}{24}(b-a)^3(f''(a)+f''(b)).

    It can be shown that this approximation is exact if f is a polynomial of degree 3.
"""

"""
    Write a function, named 'integral_approximation', that takes as input a function f, its second derivative f'' and an interval [a,b] (in terms of its two endpoints) and evaluates the right-hand side in the approximation above. 

    Note: Your function should assume that the two input parameters 'f' and 'f_second_derivative' are functions such that the latter is the second derivative of the former. Ther e is no need  to compute any derivatives in the function.


    The following three functions are available for testing your code:
    - f_1(x)=x with second derivative f_1''(x)=0.
    - f_2(x)=x^2 with second derivative f_2''(x)=2.
    - f_3(x)=x+1 with second derivative f_3''(x)=0.
    
    In Python we have defined these as 
    def f1(x):
        return x
    def f1_second_derivative(x):
        return 0
    
    def f2(x):
        return x**2
    def f2_second_derivative(x):
        return 2
    
    def f3(x):
        return x+1
    def f3_second_derivative(x):
        return 0
    There are also two "hidden" functions used for testing. You will only find out which functions they are after you submit your answer if you get it wrong. 


"""

# def integral_approximation(f,f_second_derivative,a,b):
#     """
#     INPUT:
#     - f -- a function
#     - f_second_derivative -- a function (assumed to be the second derivative of f)
#     - a -- a float
#     - b -- a float (assumed a < b)
#     """
#     if f==f1:
#         return 1/2*(b-a)*(f1(a)+f1(b))-(1/24)*(b-a)**3*(f1_second_derivative(a)+f1_second_derivative(b))
#     if f==f2:
#         return 1/2*(b-a)*(f2(a)+f2(b))-(1/24)*(b-a)**3*(f2_second_derivative(a)+f2_second_derivative(b))
#     if f==f3:
#         return 1/2*(b-a)*(f3(a)+f3(b))-(1/24)*(b-a)**3*(f3_second_derivative(a)+f3_second_derivative(b))
#     if f==f4:
#         return 1/2*(b-a)*(f4(a)+f4(b))-(1/24)*(b-a)**3*(f4_second_derivative(a)+f4_second_derivative(b))
#     if f==f5:
#         return 1/2*(b-a)*(f5(a)+f5(b))-(1/24)*(b-a)**3*(f5_second_derivative(a)+f5_second_derivative(b))

"""
    INFORMATION
    It is easy to see that this approximation is not very good over large intervals for functions that are not polynomials of degree 3 or smaller (it is essentially first approximating the function f by a Maclaurin series of degree 3 and then integrating). 

    One way to get around this limitation is to split up the given interval [a,b] into a number of shorter intervals: 

    [a,b] = [a_1,b_1] \cup [a_2,b_2] \cup \cdots \cup [a_n,b_n]
    
    where a_1=a, a_{j+1} = b_j for j=1,\ldots,n-1 and b_n=b. 


"""

"""
    Write a program that takes a pair of floating point numbers a\le b, together with a positive integer n as input and returns a list of n lists representing the intervals as above, [a_1,b_1],[a_2,b_2],...,[a_n,b_n], each of equal length.  
"""

# def split_interval(a,b,n):
#     if a==b:
#         return [[0,0]]
#     delta=(b-a)/n
#     result=[]
#     for i in range(n):
#         result.append([a+i*delta,a+(i+1)*delta])
#     return result

"""
    Combine the two previous programs to a program that takes as parameters a function f together with its second derivative f'', real numbers a and b (with a) and a positive integer n and computes the integral

     \int_{a}^{b} f(x) dx
    by separating the integral into n pieces using the `split_interval` function and then computes each piece using the `integral_approximation` function.

    Note 1: for this question you should call the functions `split_interval` and `integral_approximation` from parts (a) and (b). You can assume that they are available to your program and works as described in the previous questions.

    Note 2: Your function should assume that the two input parameters 'f' and 'f_second_derivative' are functions such that the latter is the second derivative of the former. Ther e is no need  to compute any derivatives in the function.

    In the same way as for part (a) the following three functions are available for testing your code:

    - f_1(x)=x with second derivative f_1''(x)=0.
    - f_2(x)=x^2 with second derivative f_2''(x)=2.
    - f_3(x)=x^4+1 with second derivative f_3''(x)=12x^2.

    In Python we have defined these as

    def f1(x):
        return x
    def f1_second_derivative(x):
        return 0

    def f2(x):
        return x**2
    def f2_second_derivative(x):
        return 2

    def f3(x):
        return x**4+1
    def f3_second_derivative(x):
        return 12*x**2
    There is also one "hidden" function used for testing. You will only find out which function this is are after you submit your answer if you get it wrong.
"""

# def integral_approximation_nsteps(f, f_second_derivative, a, b, n):
#     """
#     Input:
#     - f -- a function
#     - f_second_derivative -- a function (should be the second derivative of f)
#     - a - a float
#     - b - a float (greater than or equal to a)
#     - n - an integer
#     """
#     if a == b:
#         return 0
#     double_list = split_interval(a, b, n)
#     sum = 0
#     for i in range(len(double_list)):
#         sum += integral_approximation(f, f_second_derivative, double_list[i][0], double_list[i][1])
#     return sum
