def insertion_sort(data):
  n = len(data)
  for i in range(1, n):
    key = data[i]
    j = i - 1
    while j >= 0 and data[j] > key:
      data[j + 1] = data[j]
      j -= 1
    data[j + 1] = key
  return data

angka = [12, 11, 13, 5, 6]
print("Data sebelum diurutkan:", angka)
print("Data setelah Insertion Sort:", insertion_sort(angka))