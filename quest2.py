trimed_list=[]
nums=[2,2,2,11,7,2,7,75,8,15,75,75]
nums.sort()
print(nums)
for i in range(len(nums)-1):
    if nums[i]==nums[i+1] :
        continue
    else:
        trimed_list.append(nums[i])

res=len(trimed_list)-1
print(res)

