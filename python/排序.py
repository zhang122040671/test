def abc():
    nums=[36,56,89,43,26,28,12]
    for i in range(6,-1,-1):
        temp=nums[i]
        nums[i]=max(nums[0:i+1])
        nums[nums.index(max(nums[0:i+1]))]= temp
    print(nums)
abc()


nums=[36,56,89,43,26,28,12]
for i in range(6,-1,-1):
    temp=nums[i]
    nums[i]=min(nums[0:i+1])
    nums[nums.index(min(nums[0:i+1]))]= temp
print(nums)


nums=[36,56,89,43,26,28,12]
for i in range(6,-1,-1):
    nums[i],nums[nums.index(min(nums[0:i+1]))]= nums[nums.index(min(nums[0:i+1]))],nums[i],
print(nums)


