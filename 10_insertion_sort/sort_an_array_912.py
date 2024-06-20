def main():
    nums = [5,1,1,2,0,0]
    print(sortArray(nums))
    
def sortArray(nums: list[int]) -> list[int]:
    for i in range(len(nums)):
        j = i - 1
        while j >= 0 and nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]
            j -= 1
    return nums

main()