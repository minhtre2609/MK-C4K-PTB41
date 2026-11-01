def tongchan(n):
    tong = 0
    for i in range (2, n + 1, 2):
        tong += i
    return tong

n = int(input("Enter a number: "))
sum_x = tongchan(n)
print(sum_x)

