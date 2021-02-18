# 퀵정렬

number = [40,35,27,50,75]


def quickSort(array):

    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [item for item in array[1:] if item <= pivot]
        most = [item for item in array[1:] if item > pivot]
        return quickSort(less) + [pivot] + quickSort(most)


print(quickSort(number))