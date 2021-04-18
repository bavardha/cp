arr = list(map(int,input().split()))
n=len(arr)

maxi=arr[0]
ans=0
for i in range(n):
    maxi=max(maxi,arr[i])
    if(i==maxi):
        ans+=1
print(ans)

#accepted
#https://leetcode.com/problems/max-chunks-to-make-sorted