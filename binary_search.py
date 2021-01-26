nums = list(map(int, input().split()))
ele = int(input())
leng = len(nums)
res = 'Element Not Found'
beg = 0
last = leng - 1
mid = leng // 2

if(leng%2 != 0):
    while(beg <= last):
        if(ele == nums[mid]):
            res = f'Element {ele} found at position {mid +1}'
            break
        elif(ele < nums[mid]):
            last = mid
            mid = mid // 2
        elif (ele > nums[mid]):
            beg = mid + 1
            mid = (beg + last) // 2
else:
    while(beg <= last):
        if(ele == nums[mid-1]):
            res = f'Element {ele} found at position {mid}'
            break
        elif(ele == nums[mid]):
            res = f'Element {ele} found at position {mid+1}'
            break
        elif(ele < nums[mid-1]):
            last = mid - 1
            mid = (beg + last) // 2
        elif(ele > nums[mid]):
            beg = mid
            mid = beg+last//2
        
print(res)
