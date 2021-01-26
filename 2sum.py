nums=list(map(int, input().split()))
target=int(input())
leng=len(nums)
res=[]
key_values = {}
for i in range(leng):
    foo = target - nums[i]
    if foo in key_values:
        return [key_values[foo], i]
    key_values[nums[i]] = i
print(res)