
def binarySearch1(arr, target):
    """
    定义：在[l...r]的范围里寻找target, 因为这里定义是需要将r归入范围区间, inclusive，所以while循环的边界需要包含r
    :param arr:
    :param target:
    :return:
    """
    l = 0               # index of the first element
    r = len(arr) - 1    # index of the last element
    while l <= r:
        mid = l + (r - l) / 2
        if arr[mid] == target:
            return mid
        elif target > arr[mid]:
            l = mid + 1     # 明确区间的要求，只要使用过的，一律绕过。
        else:
            r = mid - 1     # 明确区间的要求，只要使用过的，一律绕过。
    return -1


def binarySearch2(arr, target):
    """
    定义：在[l...r)的范围里寻找target, 因为这里定义是不需要将end归入范围区间 exclusive，
    所以while循环的边界小于End即可，因为length本身长度会比index大1相对应的，
    每次target的value小于arr[mid]的时候，我们在重新定义新的end时候，也选择exclusive的模式，r = mid即可
    :param arr:
    :param target:
    :return:
    """
    l = 0           # index of the first element
    r = len(arr)    # r-1 is the index of the last element
    while l < r:
        mid = l + (r - l) / 2
        if arr[mid] == target:
            return mid
        elif target > arr[mid]:
            l = mid + 1     # mid is not the target, so it should be exclusive
        else:
            r = mid         # mid is the right bounday, it is alreay exclusive
    return -1


def binarySearch3(arr, target):
    """
    只是把边界的其中一个写错，也就是右边的边界值写错，如果两者同时都写错的话，可能会造成死循环。
    :param arr:
    :param target:
    :return:
    """
    l = 0
    r = len(arr) - 1    # inclusive
    while l <= r:
        mid = l + (r - l) / 2
        if arr[mid] == target:
            return mid
        elif target > arr[mid]:
            l = mid
        else:
            r = mid
    return -1


def binarySearch4(arr, target):
    """
    采用 [l, r] 的搜索范围。
    :param arr:
    :param target:
    :return:
    """
    l = 0
    r = len(arr) - 1
    while l <= r:
        mid = l + (r - l) / 2
        if target == arr[mid]:
            return mid
        elif target > arr[mid]:
            l = mid + 1
        else:
            r = mid - 1
    return -1


def binarySearch5(arr, target):
    """
    [l, r]
    i.e. l <= r,
    :param arr:
    :param target:
    :return:
    """
    l = 0
    r = len(arr) - 1
    while l+1 < r:  # i.e. l < r - 1,
        mid = l + (r - l) // 2
        if target == arr[mid]:
            return mid
        elif target > arr[mid]:
            l = mid
        else:
            r = mid

    if arr[l] == target:
        return l
    if arr[r] == target:
        return r
    return -1




