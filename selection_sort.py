def selection_sort(arr):
    n = len(arr)
    # Проходим по всем элементам массива
    for i in range(n):
        # Находим индекс минимального элемента в оставшейся части массива
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Меняем местами текущий элемент с минимальным элементом
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


# Пример использования
if __name__ == "__main__":
    example_list = [64, 25, 12, 22, 11]
    print("Исходный список:", example_list)
    sorted_list = selection_sort(example_list)
    print("Отсортированный список:", sorted_list)