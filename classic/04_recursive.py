def sum_list(arr):
    if len(arr) <= 1:
        return arr[0]
    return arr[0] + sum_list(arr[1:])


def num_list_elements(arr):
    if len(arr) <= 1:
        return 1
    return 1 + num_list_elements(arr[1:])


def find_max_element(arr):
    if len(arr) <= 1:
        return arr[0]
    max_of_rest = find_max_element(arr[1:])
    if arr[0] > max_of_rest:
        return arr[0]
    else:
        return max_of_rest


def binary_search(arr, target, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    if low > high:
        return None
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(arr, target, low=mid + 1, high=high)
    elif arr[mid] > target:
        return binary_search(arr, target, low=low, high=mid)


if __name__ == '__main__':
    assert sum_list(arr=[1, 3, 2, 4]) == 10
    assert sum_list(arr=[1, 3, 2]) == 6

    assert num_list_elements(arr=[1, 3, 4]) == 3
    assert num_list_elements(arr=[-1, 0, 1, 2]) == 4

    assert find_max_element(arr=[-1, 3, 6, 5]) == 6
    assert find_max_element(arr=[-1, 9, 6, 5]) == 9

    assert binary_search(arr=[-1, 0, 1, 3, 4, 5], target=3)
