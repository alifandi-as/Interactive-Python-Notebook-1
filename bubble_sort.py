def bubble_sort(data):
  n = len(data)
  for i in range(n):
    for j in range(0, n - i - 1):
      if data[j] > data[j + 1]:
        data[j], data[j + 1] = data[j + 1], data[j]
  return data

angka = [64, 34, 25, 12, 22, 11, 90]
print("Data sebelum diurutkan:", angka)
print("Data setelah Bubble Sort:", bubble_sort(angka))