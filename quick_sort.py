#内存溢出
'''def quick_sort(res,left,right):
    if res is None:
        return -1
    if not res:
        return 0
    if len(res) == 1:
        return res
    left,right = 0,len(res)-1
    l = left
    r = right
    key = res[left]
    while l != r:
        while res[r] >= key and l < r:
            r -= 1
        while res[l] <= key and l < r:
            l += 1
        if l < r:
            res[l],res[r] = res[r],res[l]

    if l == r:
        key,res[l] = res[l],key

    quick_sort(res,left,l-1)
    quick_sort(res,l+1,right)



a = [3,1,4,9,5,3,2,6]
b = quick_sort(a,0,len(a)-1)
print(b)'''

#分治法：
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x < pivot]
        mid = [y for y in arr[0:] if y == pivot]
        right = [z for z in arr[1:] if z > pivot]
        return quick_sort(left)+mid+quick_sort(right)

a = [3,1,4,9,5,3,2,6]
print(quick_sort((a)))