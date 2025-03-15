def bubble_sort(arr):
    n = len(arr)
    # Проходим по всем элементам
    for i in range(n):
        # Флаг для оптимизации (если обменов не было - массив отсортирован)
        swapped = False
        # Последние i элементов уже отсортированы, поэтому не проверяем их
        for j in range(0, n - i - 1):
            # Если текущий элемент больше следующего - меняем местами
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # Если не было обменов - прерываем сортировку
        if not swapped:
            break
    return arr


# Пример использования
if __name__ == "__main__":
    example_list = [64, 34, 25, 12, 22, 11, 90]
    print("Исходный список:", example_list)
    sorted_list = bubble_sort(example_list)
    print("Отсортированный список:", sorted_list)