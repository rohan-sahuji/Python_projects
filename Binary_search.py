# Prgram for binary search

def binary_search(list, element):
    start = 0
    mid = 0
    end = len(list)
    step = 0

    while(start<=end):
        print('Step',step, str(list[start:end+1]))
        step = step + 1
        mid = (start+end)//2
        if element == list[mid]:
            print('The index of target element is:',mid)
            break
        elif element < list[mid]:
            end = mid-1
        else:
            start = mid+1

    return -1

my_list = [1,2,3,4,5,6,7,8,9]
target = 7
binary_search(my_list,target)