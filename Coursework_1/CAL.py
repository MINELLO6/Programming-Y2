# import math
#
# def bernoulli(m):
#     if m == 0:
#         return 1
#     else:
#         sum = 0
#         for k in range(m):
#             sum += -math.comb(m, k) * bernoulli(k) / (m - k + 1)
#     return sum


# 不知道要不要写一个assert来限制m的大小

# result
# print(bernoulli(0))
# print(bernoulli(1))
# print(bernoulli(2))
# print(bernoulli(3))
# print(bernoulli(4))
# print(bernoulli(5))
# print(bernoulli(12))

# tests
from nose.tools import assert_equal, assert_almost_equal


# assert_equal(bernoulli(0),1)
# assert_equal(bernoulli(1),-0.5)
# assert_almost_equal(bernoulli(2),1./6.,delta=1e-12)
# assert_almost_equal(bernoulli(6),1./42.,delta=1e-12)
# assert_almost_equal(bernoulli(11),0.0,delta=1e-12)
# assert_almost_equal(bernoulli(12),-691/2730,delta=1e-12)

# def pn(n, x):
#     sum = 0
#     for i in range(1, n + 1):
#         sum += bernoulli(2 * i) / (math.factorial(2 * i)) * (-4) ** i * (1 - 4 ** i) * x ** (2 * i - 1)
#     return sum

# assert_almost_equal(pn(1,0.5),0.5,delta=1e-8)
# assert_almost_equal(pn(2,0.5),0.54166666666666,delta=1e-8)
# assert_almost_equal(pn(3,0.5),0.54583333333333,delta=1e-8)
# 未知
# 未知
# 未知

# using pylab to plot a graph
# p2要不要画。。。
# import pylab
# def draw_pn_plot():
#     xv = pylab.linspace(-pylab.pi/3,pylab.pi/3,100)
#     yv = pylab.tan(xv)
#     p1=[pn(1,x) for x in xv]
#     p2=[pn(2,x) for x in xv]
#     p3=[pn(3,x) for x in xv]
#     pylab.plot(xv,yv,label=r"$\tan(x)$")
#     pylab.plot(xv,p1,label="$p_1$")
#     pylab.plot(xv,p2,label="$p_2$")
#     pylab.plot(xv,p3,label="$p_3$")
#     pylab.legend(loc='lower right')
#     pylab.plot(xv,p1)
#     pylab.plot(xv,p2)
#     pylab.plot(xv,p3)
#     pylab.xlabel('$x$')
#     pylab.ylabel('$y$')
#     pylab.savefig('outputimage.png')
#     pylab.show()
#
# draw_pn_plot()
