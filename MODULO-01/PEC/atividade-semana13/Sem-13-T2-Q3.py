
A = []

for _ in range(20):
    A.append(int(input().strip()))

B = []

for _ in range(20):
    B.append(int(input().strip()))

C = []

for i in range(20):
    num = A[i] + B[i]
    C.append(num)

print(A)
print(B)
print(C)
