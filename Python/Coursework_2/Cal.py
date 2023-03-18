# # import numpy as np
# #
# # def estimate_pi_monte_carlo(Ntotal):
# #     if not (isinstance(Ntotal, int) and Ntotal > 0):
# #         raise ValueError(f"This function only accepts input of positive integer!")
# #     points = (2*np.random.uniform(size=(Ntotal,2)))-1
# #     N_disc=0
# #     N_total=0
# #     for i in range(0,Ntotal):
# #         if points[i][0]**2+points[i][1]**2 <= 1:
# #             N_disc+=1
# #         else:
# #             N_total+=1
# #     return N_disc/Ntotal*4
#
#
#
# # import numpy as np
# # import matplotlib.pyplot as plt
# # import random
# # from matplotlib.patches import Circle,Rectangle
# # def draw_monte_carlo(Ntotal):
# #     fig = plt.figure()
# #     ax1 = fig.add_subplot(121)
# #     rectangle = Rectangle((-1.0,-1.0),2.0,2.0,color='red')
# #     circle = Circle((0.0,0.0),1,color='green')
# #     ax1.add_patch(rectangle)
# #     ax1.add_patch(circle)
# #     ax1.set_xlim(-1,1)
# #     ax1.set_ylim(-1,1)
# #     ax1.set_xticks([-1,-0.5,0,0.5,1])
# #     ax1.set_yticks([-1,-0.5,0,0.5,1])
# #     ax1.set_aspect(1)
# #     ax1.set_xlabel('$x$')
# #     ax1.set_ylabel('$y$')
# #     ax1.set_title("Diagrammatic sketch")
# #
# #     ax2 = fig.add_subplot(122)
# #     ax2.add_patch(Circle((0.0,0.0),1,edgecolor='blue',fill=0))
# #     points = (2*np.random.uniform(size=(250,2)))-1
# #     list_in_x=[]
# #     list_in_y=[]
# #     list_out_x=[]
# #     list_out_y=[]
# #     for i in range(0,250):
# #         if points[i][0]**2+points[i][1]**2 <= 1:
# #             list_in_x.append(points[i][0])
# #             list_in_y.append(points[i][1])
# #         else:
# #             list_out_x.append(points[i][0])
# #             list_out_y.append(points[i][1])
# #     ax2.scatter(list_in_x, list_in_y, color='g', s=10)
# #     ax2.scatter(list_out_x, list_out_y, color='r', s=10)
# #     ax2.set_xlim(-1,1)
# #     ax2.set_ylim(-1,1)
# #     ax2.set_xticks([-1,-0.5,0,0.5,1])
# #     ax2.set_yticks([-1,-0.5,0,0.5,1])
# #     ax2.set_aspect(1)
# #     ax2.set_xlabel('$x$')
# #     ax2.set_ylabel('$y$')
# #     ax2.set_title("The scatter chart")
# #
# #     plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=0.5, hspace=None)
# #     plt.suptitle("the graph of the Monte Carlo method of approximating $\pi$",x=0.5,y=0.85)
# #     fig.savefig('outputimage.png')
# #
# #
# # draw_monte_carlo(250)
#
# import numpy as np
# def riemann_approximation(f, a, b, n):
#     if (a < b) and not (isinstance(a, float) and isinstance(b, float)):
#         raise ValueError("a nd b should be floats with a < b")
#     if (not isinstance(n, int)) or n <= 0:
#         raise ValueError("a should be a positive integer")
#     if not callable(f):
#         raise ValueError("f should be a callable function")
#     my_data = np.linspace(a,b,n+1,retstep=True,endpoint=True)
#     my_list = my_data[0]
#     step = my_data[1]
#     riemann_sum = 0
#     for i in range(len(my_list)-1):
#         riemann_sum = riemann_sum + step * f(my_list[i])
#     return riemann_sum
#
