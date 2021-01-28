nums = [-1,0,1,2,-1,-4]
leng=len(nums)
res=[]
for i in range(leng-2):
    for j in range(i+1, leng-1):
        for k in range(j+1, leng):
            if(nums[i]+nums[j]+nums[k] == 0):
                res.append([nums[i],nums[j],nums[k]])
res_set = set(res)
res_list = list(res_set)
print(res_list)