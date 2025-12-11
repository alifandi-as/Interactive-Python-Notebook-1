def selection_sort(data):
  n = len(data)
  for i in range(n):
    min_index = i
    for j in range(i + 1, n):
      if data[j] < data[min_index]:
        min_index = j
    data[i], data[min_index] = data[min_index], data[i]
  return data

angka = [64, 25, 12, 22, 11]
print("Data sebelum diurutkan:", angka)
print("Data setelah Selection Sort:", selection_sort(angka))