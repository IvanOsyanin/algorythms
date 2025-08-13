class BubbleSort:
    """Пузырьковая сортировка.
    Алгоритм работает за O(n²) времени.
    """
    @staticmethod
    def sort(data):
        last_index = len(data) - 1
        swapped = True
        # Цикл будет выполняться, если флаг swapped = True.
        # Это значение устанавливается при первом проходе и
        # в случае, если на предыдущем проходе были перестановки.
        # Если перестановок не было, то цикл перестанет выполняться.
        while swapped:
            swapped = False
            for idx in range(last_index):
                if data[idx] > data[idx + 1]:
                    data[idx], data[idx + 1] = data[idx + 1], data[idx]
                    swapped = True
            last_index -= 1
        return data


if __name__ == '__main__':
    bubble_sort = BubbleSort()
    sorted = bubble_sort.sort(data=[3, 1, 4, 6, 5, 7, 2])
    assert sorted == [1, 2, 3, 4, 5, 6, 7]
