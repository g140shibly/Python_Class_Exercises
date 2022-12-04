def Two_sum(nums,target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            sum=nums[i]+nums[j]
            if sum==target:
                return [i,j]

nums=[2,7,11,15]
target=9
print(Two_sum(nums,target))
nums=[3,2,4]
target=6
print(Two_sum(nums,target))
nums = [3,3]
target=6
print(Two_sum(nums,target))