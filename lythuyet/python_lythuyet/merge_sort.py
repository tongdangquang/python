n = int (input("Nhập số lượng phần tử: "))
m = []
for i in range(n):
    m.append(int(input(f"m[{i}] = ")))

def merge(m, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid
    a1 = []
    a2 = []
    for i in range(n1):
        a1.append(m[left + i])
    for i in range(n2):
        a2.append(m[mid + 1 + i])

    i = 0
    j = 0
    k = left
    while i < n1 and j < n2:
        if a1[i] < a2[j]:
            m[k] = a1[i]
            i += 1
        else:
            m[k] = a2[j]
            j += 1
        k += 1
    while i < n1:
        m[k] = a1[i]
        i += 1
        k += 1
    while j < n2:
        m[k] = a2[j]
        j += 1
        k += 1

def merge_sort(m, left, right):
    if(left < right):
        mid = (left + right)//2
        merge_sort(m, left, mid)
        merge_sort(m, mid + 1, right)
        merge(m, left, mid, right)

print(f"Mảng vừa nhập: {m}")
merge_sort(m, 0, n - 1)
print(f"Mảng đã sắp xếp: {m}")