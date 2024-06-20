class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value

def main():
    pairs = [Pair(5, "apple"), Pair(2, "banana"), Pair(9, "cherry"), Pair(1, "date"), Pair(9, "elderberry")]
    pairs = [Pair(3, "cat"), Pair(2, "dog"), Pair(3, "bird")]
    nums = [5, 2, 3, 1]
    print(pairs)
    # print(merge_sort(nums))
    sorted_pairs = merge_sort_pairs(pairs)
    for i in range(len(pairs)):
        print(sorted_pairs[i].value)

    
def merge_sort_pairs(pairs):
    if len(pairs) <= 1:
        return pairs
    
    s = 0
    e = len(pairs) -1
    m = e // 2 + 1
    sub1 = merge_sort_pairs(pairs[s:m])
    sub2 = merge_sort_pairs(pairs[m:])
    
    merged = merge_pairs(sub1, sub2)
    
    return merged
    

def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    
    s = 0
    e = len(nums) - 1
    m = e // 2 + 1
    sub1 = merge_sort(nums[s:m])
    sub2 = merge_sort(nums[m:])
    
    merged = merge(sub1, sub2)

    return merged


def merge_pairs(pair1, pair2):
    n1, n2 = len(pair1), len(pair2)
    merged = [None] * (n1 + n2)
    
    i, j, k = 0, 0, 0
    while i < len(pair1) and j < len(pair2):
        if pair1[i].key <= pair2[j].key:
            merged[k] = pair1[i]
            k += 1
            i += 1
        else:
            merged[k] = pair2[j]
            k += 1
            j += 1
            
    while i < len(pair1):
        merged[k] = pair1[i]
        k += 1
        i += 1
        
    while j < len(pair2):
        merged[k] = pair2[j]
        k += 1
        j += 1
        
    return merged


def merge(arr1, arr2):
    n1, n2 = len(arr1), len(arr2)
    merged = [None] * (n1 + n2)
    
    i, j, k = 0, 0, 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            merged[k] = arr1[i]
            k += 1
            i += 1
        else:
            merged[k] = arr2[j]
            k += 1
            j += 1
    
    while i < len(arr1):
        merged[k] = arr1[i]
        k += 1
        i += 1
        
    while j < len(arr2):
        merged[k] = arr2[j]
        k += 1
        j += 1
    
    return merged

main()