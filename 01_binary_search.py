from typing import List, Optional, Union


def binary_search(
    arr: List[Union[int, float]],
    target: Union[int, float]
) -> Optional[int]:
    """Алгоритм бинарного поиска.
    Временная сложность: O(log n)
    Пространственная сложность: O(1)
    """
    if not arr:
        raise ValueError("Массив не может быть пустым")

    # Проверяем, что массив отсортирован
    if arr != sorted(arr):
        raise ValueError(
            "Массив должен быть отсортирован"
        )

    low, high = 0, len(arr) - 1

    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return None  # Элемент не найден


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
    if not arr:
        raise ValueError("Массив не может быть пустым")

    # Проверяем, что массив отсортирован только при первом вызове
    if high is None:
        if arr != sorted(arr):
            raise ValueError(
                "Массив должен быть отсортирован"
            )
        high = len(arr) - 1

    # Базовый случай: элемент не найден
    if low > high:
        return None

    mid = low + (high - low) // 2  # Избегаем переполнения для больших чисел

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, high)
    else:
        return binary_search_recursive(arr, target, low, mid - 1)
