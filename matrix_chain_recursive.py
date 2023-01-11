# Python implementation of CLRSe3.MATRIX-CHAIN-ORDER
import sys
def matrix_chain_recursive(p, i, j):
  if i == j: # m[i,j]=0 if i==j Eq.15.7
    return 0

  m = sys.maxsize
  for k in range(i, j): # k = i,...,j-1

    q = (matrix_chain_recursive(p, i, k) # m[i,k]
      + matrix_chain_recursive(p, k + 1, j) # m[k+1,j]
      + p[i-1] * p[k] * p[j]) # pqr=p_{i-1} p_k p_j

    if q < m: # q = min(m[i,k] + m[k+1,j] + pqr)
      m = q;
  return m;

dimension_table = [10, 100, 5, 50];
n = len(dimension_table); # #matrices=n-1
print("#scalar multiplications:",
	matrix_chain_recursive(dimension_table, 1, n-1));