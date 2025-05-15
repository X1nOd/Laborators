nums = list(map(int, input().split()))
nums.sort()

option1 = nums[-1] * nums[-2] * nums[-3]
option2 = nums[0] * nums[1] * nums[-1]

if option1 >= option2:
    print(nums[-3], nums[-2], nums[-1])
else:
    print(nums[0], nums[1], nums[-1])