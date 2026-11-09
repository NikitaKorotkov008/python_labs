def linear_search(nums, x):
    """Индекс первого вхождения x или -1. Время O(n)."""
    for i in range(len(nums)):
        if nums[i] == x:
            return i
    else:
        return -1

def binary_search(sorted_nums, x):
    """Индекс любого вхождения x или -1. Время O(log n).

    Список должен быть отсортирован по возрастанию.
    На неотсортированном списке результат не определён.
    """
    l = 0
    r = len(sorted_nums)-1
    while l <= r:
        mid = (r+l)//2
        if sorted_nums[mid] == x:
            return mid
        elif sorted_nums[mid] < x:
            l = mid+1
        elif sorted_nums[mid]>x:
            r = mid-1
    return -1

def two_sum_brute(nums, target):
    """Пара индексов (i, j), i < j, с суммой target или None. Время O(n²)."""
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return (i, j)

    return None

def two_sum_fast(nums, target):
    """Пара индексов (i, j), i < j, с суммой target или None.

    Один проход со словарём: в среднем O(n) времени и O(n) памяти.
    """
    num = {}
    for i in range(len(nums)):
        ostatok = target - nums[i]
        if ostatok in num:
            return (num[ostatok], i)
        else:
            num[nums[i]] = i
    return None
