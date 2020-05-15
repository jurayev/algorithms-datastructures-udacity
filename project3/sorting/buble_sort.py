l = [16,49,3,12,56,49,55,22,13,46,19,55,46,13,25,56,9,48,45]

"""
Complexities:
Runtime O(n^2)
Space O(1)
"""
def bubble_sort_1(l):
    for _ in range(len(l)):
        for j in range(len(l)-1):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]

bubble_sort_1(l)
print(l)
print ("Pass" if (l[0] == 3) else "Fail")