from typing import List, Optional, Union


def binary_search(
    arr: List[Union[int, float]],
    target: Union[int, float]
) -> Optional[int]:
    """Алгоритм бинарного поиска.
    Временная сложность: O(log n)
    Пространственная сложность: O(1)
    """
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (high + low) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return None


def binary_search_recursive(
    arr: List[Union[int, float]],
    target: Union[int, float],
    low: int = 0,
    high: Optional[int] = None
) -> Optional[int]:
    """Алгоритм рекурсивного бинарного поиска
    Временная сложность: O(log n)
    Пространственная сложность: O(log n) из-за рекурсии
    """
    if high is None:
        high = len(arr) - 1

    if low > high:
        return None

    mid = (low + high) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, high)
    else:
        return binary_search_recursive(arr, target, low, mid - 1)


def test_binary_search():
    """Тестирование функций бинарного поиска."""
    # Тестовые данные
    arr = [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    # Тестируем обычный бинарный поиск
    print("Тестирование обычного бинарного поиска:")
    assert binary_search(arr, -1) == 0
    assert binary_search(arr, 0) == 1
    assert binary_search(arr, 1) == 2
    assert binary_search(arr, 2) == 3
    assert binary_search(arr, 4) == 5
    assert binary_search(arr, 8) == 9
    assert binary_search(arr, 9) == 10

    # Тестируем случаи, когда элемент не найден
    assert binary_search(arr, 10) is None
    assert binary_search(arr, -2) is None
    assert binary_search(arr, 5.5) is None

    print("✓ Обычный бинарный поиск работает корректно")

    # Тестируем рекурсивный бинарный поиск
    print("\nТестирование рекурсивного бинарного поиска:")
    assert binary_search_recursive(arr, -1) == 0
    assert binary_search_recursive(arr, 0) == 1
    assert binary_search_recursive(arr, 1) == 2
    assert binary_search_recursive(arr, 2) == 3
    assert binary_search_recursive(arr, 4) == 5
    assert binary_search_recursive(arr, 8) == 9
    assert binary_search_recursive(arr, 9) == 10

    # Тестируем случаи, когда элемент не найден
    assert binary_search_recursive(arr, 10) is None
    assert binary_search_recursive(arr, -2) is None
    assert binary_search_recursive(arr, 5.5) is None

    print("✓ Рекурсивный бинарный поиск работает корректно")

    # Тестируем граничные случаи
    print("\nТестирование граничных случаев:")

    # Массив из одного элемента
    single_arr = [42]
    assert binary_search(single_arr, 42) == 0
    assert binary_search(single_arr, 41) is None
    assert binary_search_recursive(single_arr, 42) == 0
    assert binary_search_recursive(single_arr, 41) is None

    # Массив из двух элементов
    two_arr = [1, 3]
    assert binary_search(two_arr, 1) == 0
    assert binary_search(two_arr, 3) == 1
    assert binary_search(two_arr, 2) is None
    assert binary_search_recursive(two_arr, 1) == 0
    assert binary_search_recursive(two_arr, 3) == 1
    assert binary_search_recursive(two_arr, 2) is None

    # Массив с дублирующимися элементами
    dup_arr = [1, 1, 2, 2, 3, 3]
    # Может найти любой из дублирующихся
    assert binary_search(dup_arr, 1) in [0, 1]
    assert binary_search(dup_arr, 2) in [2, 3]
    assert binary_search(dup_arr, 3) in [4, 5]

    print("✓ Граничные случаи обрабатываются корректно")

    print("\n🎉 Все тесты пройдены успешно!")


if __name__ == "__main__":
    test_binary_search()
