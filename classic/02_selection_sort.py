class Selection_sort:
    """Алгоритм сортировки выбором.
    Временная сложность O(n2)"""
    def _find_smallest_idx(self, arr):
        smallest = arr[0]
        smallest_idx = 0
        for idx in range(0, len(arr)):
            if arr[idx] < smallest:
                smallest = arr[idx]
                smallest_idx = idx
        return smallest_idx

    def sort(self, arr):
        result = []
        for i in range(len(arr)):
            smallest_idx = self._find_smallest_idx(arr)
            result.append(arr.pop(smallest_idx))
        return result


if __name__ == '__main__':
    selection_sort = Selection_sort()
    sorted = selection_sort.sort(arr=[3, 1, 4, 6, 5, 7, 2])
    assert sorted == [1, 2, 3, 4, 5, 6, 7]
