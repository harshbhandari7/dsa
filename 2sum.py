nums=list(map(int, input().split()))
target=int(input())
leng=len(nums)
res=[]
for i in range(0, leng-1):
    for j in range(i+1, leng):
        if(nums[i]+nums[j] == target):
            res = [i, j]
            break
print(res)