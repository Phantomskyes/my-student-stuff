nums = [1,2,3,4,5,6,7]

high = len(nums)-1
low = 0

while low<=high:
    mid = (low + high) // 2
    if nums[mid] == 4:
        print(nums[mid])
    elif nums[mid] < 4:
        low = mid+1
    else:
        high = mid-1

