# import numpy as np
# def find_max_column_value(A,i,j):
#     if type(A) is not np.ndarray:
#         raise ValueError("A must be a numpy array")
#     if not ((isinstance(i, (int, np.int32, np.int64))) and (isinstance(i, (int, np.int32, np.int64)))):
#         raise ValueError("i and j should be integers")
#     if (i >= A.shape[0] or i < 0) or (j >= A.shape[1] or j < 0):
#         raise IndexError("i and j should correspond to the index of A")
#     num_max = A[i][j]
#     k = 0
#     for s in range(i,A.shape[0]):
#         if A[s][j] >= num_max:
#             num_max = A[s][j]
#             k = s
#     return num_max, k
#
# def swap_rows(A,i,j):
#     if type(A) is not np.ndarray:
#         raise ValueError("A must be a numpy array")
#     if not ((isinstance(i, (int, np.int32, np.int64))) and (isinstance(i, (int, np.int32, np.int64)))):
#         raise ValueError("i and j should be integers")
#     if (i >= A.shape[0] or i < 0) or (j >= A.shape[1] or j < 0):
#         raise IndexError("i and j should correspond to the index of A")
#     B = A.copy()
#     for s in range(0, A.shape[1]):
#         num = B[i][s]
#         B[i][s] = B[j][s]
#         B[j][s] = num
#     return B
#
# def add_row(A,i,j,a):
#     if (i >= A.shape[0] or i < 0) or (j >= A.shape[1] or j < 0):
#         raise IndexError("i and j should correspond to the index of A")
#     B = A.copy()
#     for s in range(0, B.shape[1]):
#         B[i][s] = B[i][s]+a*B[j][s]
#     return B
#
#
# def Gauss_elimination(A):
#     if not isinstance(A, np.ndarray):
#         raise ValueError("A must be a NumPy array!")
#     if A.dtype != 'float64':
#         raise TypeError("A must have float64 entries!")
#     nrows,ncols = A.shape
#     B = A.copy()
#     # Iterate over columns but not exceeding the number of rows
#     for k in range(min(nrows,ncols)):
#         (max_abs_value,imax) = find_max_column_value(B,k,k)
#         if max_abs_value == 0:
#             continue
#         else:
#             B = swap_rows(B,k,imax)
#             for i in range(k+1, nrows):
#                 B = add_row(B,i,k,-B[i][k]/B[k][k])
#     for i in range(nrows):
#         for j in range(ncols):
#             if abs(B[i,j]) < min(ncols,nrows)*np.finfo(np.float32).eps:
#                 B[i,j]=0
#     return B
# 
