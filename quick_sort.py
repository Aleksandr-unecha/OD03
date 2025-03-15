def quick_sort(arr):
    # Базовый случай: если массив содержит 0 или 1 элемент, он уже отсортирован
    if len(arr) <= 1:
        return arr

    # Выбираем опорный элемент (pivot)
    pivot = arr[len(arr) // 2]  # Опорный элемент из середины массива

    # Разделяем массив на три части
    left = [x for x in arr if x < pivot]  # Элементы меньше опорного
    middle = [x for x in arr if x == pivot]  # Элементы равные опорному
    right = [x for x in arr if x > pivot]  # Элементы больше опорного

    # Рекурсивно сортируем левую и правую части, затем объединяем
    return quick_sort(left) + middle + quick_sort(right)


# Пример использования
if __name__ == "__main__":
    example_list = [3, 6, 8, 10, 1, 2, 1]
    print("Исходный список:", example_list)
    sorted_list = quick_sort(example_list)
    print("Отсортированный список:", sorted_list)