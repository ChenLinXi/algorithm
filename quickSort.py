#coding=utf-8

def QuickSort(arr, firstIndex, lastIndex):

    if firstIndex < lastIndex:
        # get divIndex which have prepared the arr to left-right type
        divIndex = Partition(arr, firstIndex, lastIndex)

        QuickSort(arr, firstIndex, divIndex)
        QuickSort(arr,  divIndex+1, lastIndex)
    else:
        return

def Partition(arr, firstIndex, lastIndex):
    # record numbers which is lower than the last number, "arr[lastIndex]"
    # default: i = firstIndex -1, "-1"
    # if arr[j] <= arr[lastIndex], then count, i += 1
    i = firstIndex - 1


    for j in range(firstIndex, lastIndex):

        # find the number which is lower than the last number, then swap then.
        if arr[j] <= arr[lastIndex]:
            # calculate the numbers of low number
            i += 1
            # swap the number which is lower than the last number, arr[lastIndex]
            arr[i], arr[j] = arr[j], arr[i]

    #　when loop is finished, swap arr[lastIndex]
    # finally, before i+1, all numbers is lower than arr[i+1]; after i+1, all numbers if bigger than arr[i+1]
    arr[i+1], arr[lastIndex] = arr[lastIndex], arr[i+1]

    # last but not list, process must get the partition and go on the next sub-process; till the sub-process is end
    return i


def main():
    array = [8, 10, 9, 6, 4, 16, 5, 13, 26, 18, 2, 45, 34, 23, 1, 7, 3]
    print array
    QuickSort(array, 0, len(array)-1)
    print array

if __name__ == "__main__":
    main()
