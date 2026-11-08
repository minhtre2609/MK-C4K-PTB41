"""
A = "MindX Technology"
for i in range (len(A)):
    print(A[i], end = " ")
print()  # Print a newline
for i in A:
    print(i, end = " ")
"""
#find(Xaucon, start, stop) tra ve vi tri dau tien cua xau con trong xau cha, neu khong tim thay thi tra ve -1
S = "abcd123" 
B = "d12"
C = "duy"
x = B in S #True
y = S.find(B)
z = S.find(C)
print(x)
print(y)
print(z)

m = S[1:5:2]  # Extract substring from index 1 to 3
print(m)

#cau truc day du cua slice [start:stop:step]
n = S[::-1] #in xau dao nguoc
print(n)

