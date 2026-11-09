def bubble_sort(nums):
    """Пузырьковая сортировка: новый список, исходный не меняется. O(n²)."""
    cop = list(nums)
    for i in range(len(cop) - 1):
        for j in range(len(cop) - 1 - i):
            if cop[j] > cop[j + 1]:
                cop[j], cop[j + 1] = cop[j + 1], cop[j]
    return cop

def insertion_sort(nums):
    """Сортировка вставками: новый список, исходный не меняется. O(n²) в худшем случае."""
    cop = list(nums)
    for i in range(1, len(cop)):
        key = cop[i]
        j = i - 1
        while j >= 0 and cop[j] > key:
            cop[j+1] = cop[j]
            j-=1

        cop[j+1] = key

    return cop

def selection_sort(nums):
    """Сортировка выбором: новый список, исходный не меняется. O(n²)."""
    cop = list(nums)
    for i in range(len(nums)):
        min_index = i
        for j in range(i+1, len(nums)):
            if cop[j] < cop[min_index]:
                min_index = j

        cop[i], cop[min_index] = cop[min_index], cop[i]
    return cop
