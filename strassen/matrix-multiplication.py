# for all functions, A and B are assumed
# to have same dimensions and also be square matrices

def add(A,B):
  
  n = len(A)
  C = [[0 for j in range(n)] for i in range(n)]
  for i in range(n):
    for j in range(n):
      C[i][j] = A[i][j] + B[i][j]
  
  return C

def neg(M):
  return [[-e for e in arr] for arr in M]

def extract(M, topleft_row, topleft_col, bottomright_row, bottomright_col):
  return [[M[i][j] for j in range(topleft_col, bottomright_col+1)] for i in range(topleft_row, bottomright_row+1)]


def multiply(A,B):
  n = len(A)
  if n == 1:
    return [[A[0][0] * B[0][0]]]
  
  A11 = extract(A, 0, 0, (n>>1)-1, (n>>1)-1)
  A12 = extract(A, 0, n>>1, (n>>1)-1, n-1)
  A21 = extract(A, n>>1, 0, n-1, (n>>1)-1)
  A22 = extract(A, n>>1, n>>1, n-1, n-1)
  
  B11 = extract(B, 0, 0, (n>>1)-1, (n>>1)-1)
  B12 = extract(B, 0, n>>1, (n>>1)-1, n-1)
  B21 = extract(B, n>>1, 0, n-1, (n>>1)-1)
  B22 = extract(B, n>>1, n>>1, n-1, n-1)

  M1 = multiply(add(A11, A22), add(B11, B22))
  M2 = multiply(add(A21, A22), B11)
  M3 = multiply(A11, add(B12, neg(B22)))
  M4 = multiply(A22, add(B21, neg(B11)))
  M5 = multiply(add(A11, A12), B22)
  M6 = multiply(add(A21, neg(A11)), add(B11, B12))
  M7 = multiply(add(A12, neg(A22)), add(B21, B22))

  topleft_matrix = add(add(add(M1, M4), neg(M5)), M7)
  bottomleft_matrix = add(M2, M4)
  topright_matrix = add(M3, M5)
  bottomright_matrix = add(add(add(M1, neg(M2)), M3), M6)

  blocks = [[topleft_matrix, topright_matrix],[bottomleft_matrix, bottomright_matrix]]

  ans = [[0 for j in range(n)] for i in range(n)]
  for i in range(n):
    for j in range(n):
      block_row, block_col = i // (n>>1), j // (n>>1)
      ans[i][j] = blocks[block_row][block_col][i - (n>>1) * block_row][j - (n>>1) * block_col]
  
  return ans


n = int(input())
if n < 0 or n & (n-1) != 0:
  print('Invalid dimension. Please enter a power of two.')
  exit(1)

A,B = [],[]
for i in range(n):
  A.append( list(map(int, input().split())) )

for i in range(n):
  B.append( list(map(int, input().split())) )

if any(len(arr) != n for arr in A) or any(len(arr) != n for arr in B):
  print('At least one row in either matrix entered has too many or too few elements.')
  exit(1)

product = multiply(A, B)
print('\n'.join([' '.join(map(str, arr)) for arr in product]), end = '')