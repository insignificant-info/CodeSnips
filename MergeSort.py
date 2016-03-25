def mergeSort(alist):
    if len(alist) > 1:
        mid = len(alist) //2
        left = alist[:mid]
        right = alist[mid:]

        mergeSort(left)
        mergeSort(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                alist[k] = left[i]
                i += 1
                k += 1
            else: 
                alist[k] = right[j]
                j += 1
                k += 1

        while i < len(left):
            alist[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            alist[k] = right[j]
            j += 1
            k += 1


templist = [5,2,6,7,8,6,4]
mergeSort(templist)
print(templist)


def mergeSort2(alist):
    if len(alist) <= 1:
        return alist
    else:
        i = 0
        j = 0
        k = 0

        mid = len(alist) // 2

        left = alist[:mid]
        right = alist[mid:]

        left = mergeSort2(left)
        right = mergeSort2(right)

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                alist[k] = left[i]
                k = k + 1
                i = i + 1
            else:
                alist[k] = right[j]
                k = k + 1
                j = j + 1

        while i < len(left):
            alist[k] = left[i]
            k = k + 1
            i = i + 1

        while j < len(right):
            alist[k] = right[j]
            k = k + 1
            j = j + 1
        return alist

templist = [5,2,6,7,8,6,4]
mergeSort2(templist)
print(templist)






