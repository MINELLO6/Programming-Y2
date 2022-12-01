# def cube_root(a, e, x0):
#     assert a > 0 and e > 0 and x0 > 0
#     n = 0
#     while abs(x0 ** 3 - a) >= e:
#         x0 = 1 / 3 * (2 * x0 + a / (x0 ** 2))
#         if abs(x0 ** 3 - a) >= e:
#             n += 1
#         else:
#             return x0, n + 1
#     return x0, n
#
#
# from nose.tools import assert_equal, assert_almost_equal, assert_raises

# 具体多次迭代的两个例子
# print(cube_root(2.0, 1e-10, 1))
# print(cube_root(3.0, 1e-10, 5))

# print(2 ** (1 / 3))
# [1, 1.3333333333333333, 1.2638888888888888, 1.259933493449977, 1.2599210500177698, 1.259921049894873]
# print(3 ** (1 / 3))
# [5, 3.373333333333333, 2.336767156007575, 1.7409788292572606, 1.4905758774387161, 1.443799436236203, 1.4422512334365245, 1.4422495703093259]
# 精度上面有所误差，当1e-10不够满足要求。但是应该不会测试更精确的值，这是由python存储float的方式决定的一定会有误差

# # 检查输出类型
# assert_equal(type(cube_root(2.0, 1e-10, 1)), tuple)
# # 检查第一次成功(0次迭代)是否符合程序
# assert_equal(cube_root(8, 1e-10, 2), (2, 0))
# # 检查多次迭代结果的数值,从左边和右边初始值进行迭代
# assert_almost_equal(cube_root(2.0, 1e-10, 1)[0], 1.259921049894873, delta=1e-8)
# assert_almost_equal(cube_root(2.0, 1e-10, 3)[0], 1.259921049894873, delta=1e-8)
# # 检查多次迭代结果的次数
# assert_almost_equal(cube_root(2.0, 1e-10, 1)[1], 5)
# # 检查Assert运行状况
# assert_raises(AssertionError, cube_root, -2, 1e-10, 1)


# def cube_root_list(a, e, x0):
#     assert a > 0 and e > 0 and x0 > 0
#     ans_list = [x0]
#     while abs(x0 ** 3 - a) >= e:
#         x0 = 1 / 3 * (2 * x0 + a / (x0 ** 2))
#         ans_list.append(x0)
#     return ans_list
#
# print(cube_root_list(20000,1e-10,1))

# print(cube_root_list(8.0, 1e-10, 2))
# print(cube_root_list(2.0, 1e-10, 1))
# print(cube_root_list(2000, 1e-10, 1))

# 测试输出类型
# assert_equal(type(cube_root_list(2.0, 1e-10, 1)), list)
# 测试初始值，保证是正确的初始迭代值
# assert_almost_equal(cube_root_list(2.0, 1e-10, 1)[0], 1.0, delta=1e-8)
# 测试最终迭代值
# assert_almost_equal(cube_root_list(2.0, 1e-10, 1)[-1], 1.259921049894873, delta=1e-8)
# 测试具体迭代数组
# 未知
# 未知

# import pylab
#
# def draw_plot(a):
#     data=cube_root_list(a,1e-10,1)
#     print(data)
#     n=pylab.linspace(0,len(data)-1,len(data))
#     pylab.scatter(n,data,linewidths=1,label="approximation of $\sqrt[3]{20000}$")
#     pylab.axhline(y=20000**(1/3),linewidth=2,color='red',label="horizontal line of $\sqrt[3]{20000}$")
#     pylab.legend(loc='upper right')
#     pylab.xlabel('$n$')
#     pylab.ylabel('$x_n$')
#     pylab.xticks(pylab.linspace(0,len(data)-1,len(data)))
#     pylab.savefig('outputimage.png')
#     pylab.show()
#
# draw_plot(20000)



