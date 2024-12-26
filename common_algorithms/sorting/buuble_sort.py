def bubble_sort(arr):
    n = len(arr) - 1
    print("Numeros na lista ", n + 1)
    for i in range(n):
        print("Passagem ", i + 1)
        print("Indice final ", n-i)
        for j in range(0, n-i):
            print("Comparando ", arr[j], ">", arr[j+1])
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

#0(n^2)

print(bubble_sort([9, 5,2,3, 6, 0, 8, 11 ]))