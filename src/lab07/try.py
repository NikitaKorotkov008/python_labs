import random
from src.lab07.sorting import bubble_sort
from src.lab07.bench import measure
from src.lab07.sorting import insertion_sort, selection_sort

nums = [random.randint(-100_000, 100_000) for _ in range(1_000_000)]

seconds = measure(lambda: selection_sort(nums), limit=60)
print("Время в секундах:", seconds)





def linear(nums, x):
    for i in range(len(nums)):
        if nums[i] == x:
            return i
    else:
        return -1


def binar(nums, x):
    l = 0 
    r = len(nums)-1
    while l <=r:
        mid = (l+r) //2
        if mid == x :
            return mid 
        if mid > x:
            r = mid-1
        if mid < x:
            l=mid+1 

    return -1


def brut(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return (i, j)
    else:
        return None 


def fast_brerute(nums, target):
    num= {}
    for i in range(len(nums)):
        ostatok = target - nums[i]
        if ostatok in num:
            return (nums[ostatok], i)
        else:
            num[ostatok] = i
    else:
        return None




def buble(nums):
    cop = list(nums)
    for i in range(len(cop)-1):
        for j in range(len(cop)-1-i):
            if cop[j] > cop[j+1]:
                cop[j], cop[j+1] = cop[j+1], cop[j]
    return cop


def insertiomn(nums):
    cop = list(nums)
    for i in range(1,len(nums)):
        key = cop[i]
        j = i-1
        while j >=0 and cop[j] > key:
            cop[j+1] = cop[j]
            j-=1
        cop[j+1] = key
    return cop



def selection(nums):
    cop = list(nums)
    for i in range(len(cop)):
        min_index=i
        for j in range(i+1, len(cop)):
            if cop[j] < cop[min_index]:
                min_index = j
        cop[i], cop[min_index] = cop[min_index], cop[i]
    return cop




def insertion(nums):
    cop = list(nums)
    for i in range(1, len(cop)):
        key = cop[i]
        j = i -1
        while j >= 0 and cop[j] > key:
            cop[j+1] = cop[j]
            j-=1
        cop[j+1] = key
    return cop



def selection(nums):
    cop = list(nums)
    for i in range(len(cop)):
        min_index = i
        for j in range(i+1, len(cop)):
            if cop[j] < cop[min_index]:
                min_index = j
        cop[j]





def inserrtion(nums):
    cop = list(nums)
    for i in range(1,len(cop)):
        key = cop[i]
        j = i-1
        while j >= 0 and cop[j] > key:
            cop[j+1] = cop[j]
            j-=1
        cop[j+1] = key 
    return cop




def selection(nums):
    cop = list(nums)
    for i in range(len(cop)):
        min_index = i 
        for j in range(i+1, len(cop)):
            if cop[min_index] > cop[j]:
                min_index = j
        cop[j], cop[min_index] = cop[min_index], cop[j]
    return cop