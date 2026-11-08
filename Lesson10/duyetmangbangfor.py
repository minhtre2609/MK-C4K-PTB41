a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(len(a)):
    print(a[i], end = "")

#append() la chen phan tu vao cuoi danh sach
#vd a.append(11) => a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
#insert() la chen phan tu vao vi tri bat ky trong danh sach insert(gia tri, vi tri)
#vd a.insert(0, 0) => a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#remove() la xoa phan tu trong danh sach remove(gia tri)
#vd a.remove(5) => a = [1, 2, 3, 4, 6, 7, 8, 9, 10]
#pop la chi dinh phan tu muon xoa trong danh sach pop(vi tri)
#vd a.pop(0) => a = [2, 3, 4, 5, 6, 7, 8, 9, 10]
#clear() la xoa toan bo phan tu trong danh sach
#vd a.clear() => a = []
#sort() la ham sap xep phan tu tu be den lon
#sort(reverse = True) la ham sap xep phan tu tu lon den be