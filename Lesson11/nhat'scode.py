s = input("Nhập ngày tháng (dd/mm/yyyy): ")
s = "Ngày " + s
s = s.replace("/", " tháng ", 1)
s = s.replace("/", " năm ", 1)
print(s)

