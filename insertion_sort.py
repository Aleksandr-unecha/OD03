def insertion_sort(arr):
    n = len(arr)
    # Проходим по всем элементам, начиная со второго
    for i in range(1, n):
        key = arr[i]  # Текущий элемент, который нужно вставить в отсортированную часть
        j = i - 1

        # Перемещаем элементы массива, которые больше `key`, на одну позицию вперед
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        # Вставляем `key` на правильную позицию
        arr[j + 1] = key

    return arr


# Пример использования
if __name__ == "__main__":
    example_list = [12, 11, 13, 5, 6]
    print("Исходный список:", example_list)
    sorted_list = insertion_sort(example_list)
    print("Отсортированный список:", sorted_list)