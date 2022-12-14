# from nose.tools import assert_equal, assert_raises
#
#
# def scalar_product(v1, v2):
#     assert type(v1) == tuple and type(v2) == tuple, "The type of v1 and v2 is tuple"
#     可以使用isinstance()来解决，作用和type()，除了返回值和有无判断继承关系的作用
#     assert len(v1) == len(v2), "Enter v1 and v2 with the same length"
#     for i in range(len(v1)):
#         assert (type(v1[i]) == int or type(v1[i]) == float) and (type(v2[i]) == int or type(v2[i]) == float), "The entries in the tuple should be int or float"
#     sum = 0
#     for i in range(len(v1)):
#         sum += v1[i] * v2[i]
#     return sum
#
#
# assert_equal(scalar_product((1, 2, 0), (-2, 1, -1)), 0)
# assert_equal(scalar_product((1, 2, 1), (-2, 1, -1)), -1)
# assert_raises(AssertionError, scalar_product, 1, 2)
#
#
# import math
# def projection(u, v):
#     assert type(u) == tuple and type(v) == tuple, "The type of u and v is tuple"
#     assert len(u) == len(v), "Enter u and v with the same length"
#     assert u.count(0) != len(u)
#     for i in range(len(u)):
#         assert (type(u[i]) == int or type(u[i]) == float) and (type(v[i]) == int or type(v[i]) == float), "The entries in the tuple should be int or float"
#     mul = scalar_product(u, v) / scalar_product(u, u)
#     s = tuple(mul * x for x in u)
#     return s
#
#
# # print(projection((1,0),(0,0)))
#
# from nose.tools import assert_equal, assert_almost_equal, assert_tuple_equal
#
# assert_equal(projection((0, 1), (1, 1)), (0, 1))
#
#
# def assert_almost_equal_vector(v, u, delta):
#     assert len(u) == len(v)
#     assert all(abs(v[i] - u[i]) < delta for i in range(len(v)))
#
#
# assert_almost_equal_vector(projection((101, 1, 0), (1, 2, 10)), (1.0197020192119193, 0.010096059596157616, 0.0), delta=1e-10)
#
# assert_almost_equal_vector(projection((1, 2), (1, 3)), (1.4, 2.8), delta=1e-10)
# assert_almost_equal_vector(projection((101, 1, 0), (1, 2, 10)), (1.0197020192119193, 0.010096059596157616, 0.0), delta=1e-10)
# assert_raises(AssertionError, projection, (-1, -1), 2)
#
#
# import math
# def projection_orthogonal(u, v):
#     assert type(u) == tuple and type(v) == tuple, "The type of u and v is tuple"
#     assert len(u) == len(v), "Enter u and v with the same length"
#     for i in range(len(u)):
#         assert (type(u[i]) == int or type(u[i]) == float) and (type(v[i]) == int or type(v[i]) == float),  "The entries in the tuple should be int or float"
#     assert u.count(0) != len(u), "u is not a zero vector"
#     proj_u = projection(u, v)
#     proj_ortho_u = ()
#     for i in range(len(u)):
#         temp = v[i] - proj_u[i]
#         proj_ortho_u += (temp,)
#     return proj_ortho_u
#
#
# assert_equal(projection_orthogonal((0, 1), (1, 1)), (1, 0))
# assert_almost_equal_vector(projection_orthogonal((1, 2), (1, 3)), (-0.4, 0.2), delta=1e-10)
# assert_almost_equal_vector(projection_orthogonal((101, 1, 0), (1, 2, 10)),
#                            (-0.019702019211919275, 1.9899039404038423, 10.0), delta=1e-10)
# assert_raises(AssertionError, projection_orthogonal, (-1, -1), 2)
#
#
# import math
# def projection_on_set(v, U):
#     for i in range(len(v)):
#         assert (type(v[i]) == int or type(v[i]) == float), "Entries in v should be int or float"
#     for i in range(len(U)):
#         for j in range(len(U[i])):
#             assert (type(U[i][j]) == float or type(U[i][j]) == int), "The entries of U's tuples should be int or float"
#     (isinstance(x,tuple) for x in U)是其他一种写法
#     for i in range(len(U)):
#         assert len(U[0]) == len(U[i]), "The tuple in U should have the same length"
#         assert type(U[i]) == tuple
#         for j in range(i + 1, len(U)):
#             assert scalar_product(U[i], U[j]) < 10 ** -10, "Vectors in U should be orthogonal!"
#     result = []
#     for i in range(len(U)):
#         dim = projection(U[i], v)
#         result.append(dim)
#     return tuple(result)
# #
#
# # print(projection_on_set((1, 5, 3), [(1, 0, 1 / 2), (1, 0, -2)]))
# # print(projection_on_set((1, 2, 3), [(1, 0, 0), (0, 1, 0), (0, 0, 1)]))
# assert_equal(projection_on_set((1, 2, 3), [(1, 0, 0), (0, 1, 0), (0, 0, 1)]), ((1.0, 0.0, 0.0), (0.0, 2.0, 0.0), (0.0, 0.0, 3.0)))
# assert_raises(AssertionError, projection_on_set, (1, 2, 3), [(1, 1, 0), (0, 1, 0), (0, 0, 1)])
# assert_raises(AssertionError, projection_on_set, (1, 2, 3, 3), [(1, 0, 0), (0, 1, 0), (0, 0, 1)])
# assert_equal(projection_on_set((1, 5, 3), [(1, 0, 1), (0, 1, 0)]), ((2.0, 0.0, 2.0), (0.0, 5.0, 0.0)))
# assert_equal(projection_on_set((1,5,3),[(1,0,1/2),(1,0,-2)]),((2.0, 0.0, 1.0), (-1.0, 0.0, 2.0)))
#
# # print(type(0) == int or type(0) == float)
