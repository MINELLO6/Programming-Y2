# import math
# import numpy as np
#
# # def estimated_relative_error(x0, x1):
# #     if x0 == 0 and x1 == 0:
# #         return 0
# #     else:
# #         return abs((x1-x0))/math.sqrt(x0**2 + x1**2)
# #
# # def secant_method(f, x0, x1, tol, kmax):
# #     if tol <= 0:
# #         raise ValueError("Please enter tol greater than 0")
# #     if kmax <= 0:
# #         raise ValueError("please enter kmax greater than 0")
# #     if x0 == x1:
# #         raise ValueError("Please make x0 and x1 are not equal")
# #     k = 0
# #     while estimated_relative_error(x0, x1) > tol:
# #         buffer = x1
# #         x1 = x1 - ((x1-x0)/(f(x1)-f(x0)))*f(x1)
# #         x0 = buffer
# #         k += 1
# #         if k > kmax:
# #             raise ArithmeticError("k is greater than kmax and no xk is found")
# #             break
# #         if estimated_relative_error(x0, x1) <= tol:
# #             break
# #
# #     return x1, estimated_relative_error(x0, x1), k
#
#
# def secant_method_list(f,x0,x1,tol,kmax):
#     if tol <= 0:
#         raise ValueError("Please enter tol greater than 0")
#     if kmax <= 0:
#         raise ValueError("please enter kmax greater than 0")
#     if x0 == x1:
#         raise ValueError("Please make x0 and x1 are not equal")
#     my_list = [(x0, f(x0)), (x1, f(x1))]
#     k = 0
#     while abs(x0-x1)/(abs(x0)+abs(x1)) > tol:
#         buffer = x1
#         x1 = x1 - ((x1-x0)/(f(x1)-f(x0)))*f(x1)
#         print(x1)
#         x0 = buffer
#         k += 1
#         my_list.append((x1, f(x1)))
#         if k > kmax:
#             raise ArithmeticError("k is greater than kmax and no xk is found")
#             break
#         if abs(x0-x1)/(abs(x0)+abs(x1)) <= tol:
#             break
#     return my_list
#
# import numpy as np
# import matplotlib.pyplot as plt
# fig = plt.figure(figsize=(20,10))
# ax = fig.add_subplot(111)
# x=np.linspace(-3,5)
# f_x = (x**3-2*x**2+2*x)/(2*x**2+1)
# line_f_x = ax.plot(x, f_x)
# points_x=[-1, 1, 0.6666666666666667, 2.8888888888888884, -1.7968024755028384]
# points_y=[-1.6666666666666667, 0.3333333333333333, 0.39215686274509803, 0.7459099015274866, -2.1257318138669765]
# ax.scatter(points_x, points_y, color='r', s=100)
# ax.scatter(points_x, [0]*5, color='k', s=100, marker='x')
# for i in range(len(points_x)-2):
#     k = (points_y[i]-points_y[i+1])/(points_x[i]-points_x[i+1])
#     b = points_y[i]-k*points_x[i]
#     my_line = k*x+b
#     # print(my_line)
#     ax.plot(x,my_line, 'g')
# # ax.plot(points_x, points_y)
# for i in range(len(points_x)):
#     ax.annotate(f'point {i}', xy=(points_x[i],points_y[i]), xytext=(points_x[i],points_y[i]+0.5),textcoords='data',
#     arrowprops=dict(arrowstyle="->", connectionstyle="arc3"))
# ax.axhline(y=0,color='k')
# ax.set_ylim(-3,3)
# # ax.set_xticks(points_x)
# ax.title.set_text('Secant Method')
# ax.set_xlabel('$x$')
# ax.set_ylabel('$y$')
# fig.savefig('outputimage.png')
