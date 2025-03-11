def merge(data, temp, low, middle, high):
    ri, ti, di = low, low, middle
    while ti < middle and di <= high:
        if data[di] < temp[ti]:
            data[ri] = data[di]
            di += 1
        else:
            data[ri] = temp[ti]
            ti += 1
        ri += 1
    while ti < middle:
        data[ri] = temp[ti]
        ti += 1
        ri += 1

def merge_sort_recursive(data, temp, low, high):
    n = high - low + 1
    middle = low + n // 2
    if n < 2:
        return
    for i in range(low, middle):
        temp[i] = data[i]
    merge_sort_recursive(temp, data, low, middle - 1)
    merge_sort_recursive(data, temp, middle, high)
    merge(data, temp, low, middle, high)

def merge_sort(data):
    n = len(data)
    temp = [0] * n
    merge_sort_recursive(data, temp, 0, n - 1)

data = [92, 471, -49, 340, 286, 406, 127, 352, 407, 78, 225, 499, 224, 83, 269, -103, 356, 137, -187, 317, 495, 82, 409, 345, 483, -108, 100, 296, 52, 19, 327, 272, 123, 34, 189, 56, 150, 12, 9, 240]
merge_sort(data)
print(data)