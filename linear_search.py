nums = list(map(int, input().split()))
ele = int(input())
leng = len(nums)
res = 'Element Not found'
for i in range(0, leng):
    if(ele == nums[i]):
        res = f'Element Found at {i+1} position'
        break
print(res)


# Multiple occurences of an element
ctr = 0
for i in range(0, leng):
    if(ele == nums[i]):
        ctr += 1
print(f'Count : {ctr}')