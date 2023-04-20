# from django.test import TestCase

# Create your tests here.

def bubble_sort(lst):
    l = len(lst) - 1
    is_sorted = False

    while not is_sorted:
        is_sorted = True
        for i in range(l):
            if lst[i] < lst[i + 1]:
                is_sorted = False
                lst[i],lst[i + 1] = lst[i + 1],lst[i]
    return lst

print(bubble_sort([11,5,3,4,99]))


