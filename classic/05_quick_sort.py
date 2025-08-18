import random

def quick_sort(arr):
    """Алгоритм быстрой сортировки
    Высота стека вызова O(log(n)) - если бьем каждый
    раз на две части, O(n) если каждый раз с края.
    Худший случай - O(n2), что происходит, если опорный
    элемент каждый раз оказывается крайним
    (например, минимальным или максимальным)."""

    if len(arr) < 2:
        return arr

    pivot = arr[random.randint(0,len(arr)-1)]

    left = [i for i in arr if i < pivot]
    middle = [x for x in arr if x == pivot]
    right = [i for i in arr if i > pivot]

    return quick_sort(left) + middle + quick_sort(right)


if __name__ == '__main__':
    arr = [4, -1, 0, 3, 2, 5, 6, 7, 9, 8]
    print(quick_sort(arr))
